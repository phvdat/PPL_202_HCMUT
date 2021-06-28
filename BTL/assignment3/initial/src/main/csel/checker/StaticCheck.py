# Pham Van Dat
# 1811892
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class NumberType(Prim):
    def __str__(self):
        return "NumberType"


class StringType(Prim):
    def __str__(self):
        return "StringType"


class BoolType(Prim):
    def __str__(self):
        return "BooleanType"


class VoidType(Type):
    def __str__(self):
        return "VoidType"


class Unknown(Type):
    def __str__(self):
        return "Unknown"

class JSONType(Type):
    def __str__(self):
        return "JSONType"


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type


@dataclass
class MType:
    intype: List[Type]
    restype: Type


@dataclass
class Symbol:
    name: str
    mtype: Type


def setType(id, c, typ):
    find = False
    for elem in c:
        for i in elem:
            if id.name == i.name:
                find = True
                i.mtype.restype = typ()
                break
        if find:
            break
def setTypeArrAccess(id, c, typ):
    find = False
    for elem in c:  
        for i in elem:
            if id.name == i.name:
                find = True
                i.mtype.restype.eletype = typ()
                break
        if find:
            break

class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("str2num", MType([StringType()], VoidType())),
            Symbol("num2str", MType([NumberType()], StringType())),
            Symbol("str2bool", MType([StringType()], VoidType)),
            Symbol("bool2str", MType([BoolType()], StringType())),

            Symbol("read", MType([], StringType())),
            Symbol("print", MType([StringType()], VoidType())),
            Symbol("printLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    # decl: List[Decl]
    def visitProgram(self, ast, c):
        c = [self.global_envi[:]]
        
        # Check main function
        is_main = False
        for x in ast.decl:
            if isinstance(x, FuncDecl) and x.name.name == 'main':
                is_main = True
                break
        if not is_main:
            raise NoEntryPoint()

        # Check Redeclare
        for x in ast.decl:
            if isinstance(x, VarDecl): 
                c[0].append(self.visit(x, c))

            elif isinstance(x, ConstDecl):
                c[0].append(self.visit(x, c))

            elif isinstance(x, FuncDecl):
                func = Symbol(x.name.name, MType([], NoneType()))
                for i in c[0]:
                    if i.name == func.name:
                        raise Redeclared(Function(), func.name)
                c[0].append(func)
                pram_lst = self.visit(x, c)
                for elem in c[0]:
                    if elem.name == x.name.name:
                        elem.mtype.intype = pram_lst


    # variable: Id
    # varDimen: List[Expr]     # empty list for scalar variable
    # typ: Type               # NoneType if empty
    # varInit: Expr           # None if no initial
    def visitVarDecl(self, ast, c):
        for i in c[0]:
            if i.name == ast.variable.name:
                raise Redeclared(Variable(), ast.variable.name)
        lst = ast.varDimen
        if lst:
            for i in lst:
                if str(self.visit(i, c)) == "NoneType":
                    raise TypeCannotBeInferred(ast)
                if str(self.visit(i, c)) != "NumberType":
                    raise TypeMismatchInExpression(ast)

        vartype = ast.typ
        vInit = None
        if ast.varInit:
            vInit = self.visit(ast.varInit, c)
        if str(vInit) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
            
        # =======================ARRAY========================
        if lst: # if array declare
            if ast.varInit:
                if not isinstance(vInit,ArrayType):     # if rhs not array type
                    if isinstance(vInit, NoneType):
                        if isinstance(ast.varInit, CallExpr): # if CallExp: need .method
                            setType(ast.varInit.method, c, ArrayType)
                        elif isinstance(ast.varInit, ArrayAccess): # if ArrayAccess: need .arr
                            setTypeArrAccess(ast.varInit.arr, c, ArrayType)
                        else:
                            setType(ast.varInit, c, ArrayType)
                    else:
                        raise TypeMismatchInStatement(ast)
                if isinstance(vartype, ArrayType):      # if type elem = arraytype => false
                    raise TypeMismatchInStatement(ast)
                if not isinstance(self.visit(ast.varInit, c), ArrayType):
                    raise TypeMismatchInStatement(ast)
                if len(lst) != len(self.visit(ast.varInit, c).dimen):
                    raise TypeMismatchInStatement(ast)
                if str(vartype) == "NoneType":
                    return Symbol(ast.variable.name, MType([], ArrayType(lst,self.visit(ast.varInit, c).eletype)))
                if str(vartype) != str(self.visit(ast.varInit, c).eletype):
                    raise TypeMismatchInStatement(ast)
            return Symbol(ast.variable.name, MType([], ArrayType(lst,vartype)))
        
        # =======================JSON========================
        if ast.varInit:
            if str(vInit) == "JSONType":
                if str(vartype) != "NoneType":
                    raise TypeMismatchInStatement(ast)
                return Symbol(ast.variable.name, MType([], JSONType()))
            if str(vartype) == "JSONType":
                if str(vInit) == "NoneType":
                    if isinstance(ast.varInit, CallExpr): # if CallExp: need .method
                        setType(ast.varInit.method, c, JSONType)
                    elif isinstance(ast.varInit, ArrayAccess): # if ArrayAccess: need .arr
                        setTypeArrAccess(ast.varInit.arr, c, JSONType)
                    else:
                        setType(ast.varInit, c, JSONType)
        # ==============NUMBER, STRING, BOOLEAN===============
        if (str(ast.typ) ==  'NoneType') and (ast.varInit is None):
            return Symbol(ast.variable.name, MType([], NoneType()))
        elif str(vartype) ==  'NoneType' and str(ast.varInit) == 'NoneType':
            raise TypeCannotBeInferred(ast)
        elif ast.varInit is None:
            return Symbol(ast.variable.name, MType([], vartype))
        elif str(ast.varInit) == 'NoneType':
            if isinstance(ast.varInit, CallExpr): # if CallExp: need .method
                setType(ast.varInit.method, c, type(vartype))
            elif isinstance(ast.varInit, ArrayAccess): # if ArrayAccess: need .arr
                setType(ast.varInit.arr, c, type(vartype))
            return Symbol(ast.variable.name, MType([], vartype))
        elif (str(ast.typ) ==  'NoneType'):
            return Symbol(ast.variable.name, MType([], vInit))
        elif str(vartype) != str(vInit):
            raise TypeMismatchInStatement(ast)
        
        return Symbol(ast.variable.name, MType([], vartype))

    # constant: Id
    # constDimen: List[Expr]       # empty list for scalar variable
    # typ: Type                   # NoneType if empty
    # constInit: Expr

    def visitConstDecl(self, ast, c):
        for i in c[0]:
            if i.name == ast.constant.name:
                raise Redeclared(Constant(), ast.constant.name)
        lst = ast.constDimen
        if lst:
            for i in lst:
                if str(self.visit(i, c)) != "NumberType":
                    raise TypeMismatchInStatement(ast)
        
        vartype = ast.typ
        vInit = self.visit(ast.constInit, c)
        if str(vInit) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        # =======================ARRAY========================
        if lst: # if array declare
            if not isinstance(vInit,ArrayType):     # if rhs not array type
                if isinstance(vInit, NoneType):
                    if isinstance(ast.constInit, CallExpr): # if CallExp: need .method
                        setType(ast.constInit.method, c, ArrayType)
                    elif isinstance(ast.constInit, ArrayAccess): # if ArrayAccess: need .arr
                        setTypeArrAccess(ast.constInit.arr, c, ArrayType)
                    else:
                        setType(ast.constInit, c, ArrayType)
                else:
                    raise TypeMismatchInStatement(ast)
            if isinstance(vartype, ArrayType):      # if type elem = arraytype => false
                raise TypeMismatchInStatement(ast)
            if not isinstance(self.visit(ast.constInit, c), ArrayType):
                raise TypeMismatchInStatement(ast)
            if len(lst) != len(self.visit(ast.constInit, c).dimen):
                raise TypeMismatchInStatement(ast)
            if str(vartype) == "NoneType":
                return Symbol(ast.constant.name, MType([], ArrayType(lst,self.visit(ast.constInit, c).eletype)))
            if str(vartype) != str(self.visit(ast.constInit, c).eletype):
                raise TypeMismatchInStatement(ast)
            return Symbol(ast.constant.name, MType([], ArrayType(lst,vartype)))
        # =======================JSON========================
        if ast.constInit:
            if str(vInit) == "JSONType":
                if str(vartype) != "NoneType":
                    raise TypeMismatchInStatement(ast)
                return Symbol(ast.constant.name, MType([], JSONType()))
            if str(vartype) == "JSONType":
                if str(vInit) == "NoneType":
                    if isinstance(ast.constInit, CallExpr): # if CallExp: need .method
                        setType(ast.constInit.method, c, JSONType)
                    elif isinstance(ast.constInit, ArrayAccess): # if ArrayAccess: need .arr
                        setTypeArrAccess(ast.constInit.arr, c, JSONType)
                    else:
                        setType(ast.constInit, c, JSONType)
        # ==============NUMBER, STRING, BOOLEAN===============
        if (str(ast.typ) ==  'NoneType') and (ast.constInit is None):
            return Symbol(ast.constant.name, MType([], NoneType()))
        elif str(vartype) ==  'NoneType' and str(ast.constInit) == 'NoneType':
            raise TypeCannotBeInferred(ast)
        elif ast.constInit is None:
            return Symbol(ast.constant.name, MType([], vartype))
        elif str(ast.constInit) == 'NoneType':
            if isinstance(ast.constInit, CallExpr): # if CallExp: need .method
                setType(ast.constInit.method, c, type(vartype))
            elif isinstance(ast.constInit, ArrayAccess): # if ArrayAccess: need .arr
                setTypeArrAccess(ast.constInit.arr, c, type(vartype))
            return Symbol(ast.constant.name, MType([], vartype))
        elif (str(ast.typ) ==  'NoneType'):
            return Symbol(ast.constant.name, MType([], vInit))
        elif str(vartype) != str(vInit):
            raise TypeMismatchInStatement(ast)
        
        return Symbol(ast.constant.name, MType([], vartype))

    # name: Id
    # param: List[VarDecl]
    # body: List[Inst]
    def visitFuncDecl(self, ast, c):

        local_envi = [[]]
        para_list = [] # use to check param có bị trùng
        for param in ast.param:
            if param.variable.name in para_list:
                raise Redeclared(Parameter(), param.variable.name)
            else:
                para_list.append(param.variable.name)
                local_envi[0].append(self.visit(param, local_envi))
                        
        rt_param_lst = local_envi[:]
        local_envi = local_envi + c
        for elem in c[0]: # modify type pram_lst
            if elem.name == ast.name.name:
                elem.mtype.intype = [x.mtype.restype for x in rt_param_lst[0]]
                        
        for stmt in ast.body:
            if isinstance(stmt, VarDecl):
                local_envi[0].append(self.visit(stmt, local_envi))
            elif isinstance(stmt, ConstDecl):
                local_envi[0].append(self.visit(stmt, local_envi))
            else:
                if isinstance(stmt, Return):
                    for elem in c[0]:
                        if elem.name == ast.name.name:
                            elem.mtype.restype = self.visit(stmt, local_envi)
                else:
                    self.visit(stmt, local_envi)
        
        return [x.mtype.restype for x in rt_param_lst[0]]

    # lhs: LHS
    # rhs: Expr
    def visitAssign(self, ast, c):
        typ2=self.visit(ast.rhs,c)
        typ1=self.visit(ast.lhs,c)
        if str(typ1) == "TypeCannotBeInferred" or str(typ2) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        if type(typ1) is VoidType or type(typ2) is VoidType:
            raise TypeMismatchInStatement(ast)
        if str(typ1) == "Unknown" or str(typ2) == "Unknown":
            pass
        elif isinstance(typ1, ArrayType) and isinstance(typ2, ArrayType):
            if len(typ1.dimen) != len(typ2.dimen):
                raise TypeMismatchInStatement(ast)
            else:
                pass
        else:
            if type(typ2) is NoneType and type(typ1) is NoneType:
                raise TypeCannotBeInferred(ast)

            if type(typ1) is NoneType:
                if isinstance(ast.lhs, CallExpr): # if CallExp: need .method
                    setType(ast.lhs.method, c, type(typ2))
                elif isinstance(ast.lhs, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.lhs.arr, c, type(typ2))
                else:
                    setType(ast.lhs, c, type(typ2))
                typ1 = typ2
            elif type(typ2) is NoneType:
                if isinstance(ast.rhs, CallExpr): # if CallExp: need .method
                    setType(ast.rhs.method, c, type(typ2))
                elif isinstance(ast.rhs, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.rhs.arr, c, type(typ2))
                else:
                    setType(ast.rhs, c, type(typ1))
                typ2 = typ1
            elif str(typ1) != str(typ2):
                raise TypeMismatchInStatement(ast)
    # ifthenStmt: List[Tuple[Expr, List[Inst]]]
    # elseStmt: List[Inst]  # for Else branch, empty list if no Else
    def visitIf(self, ast, c):
        ifthemStmt = ast.ifthenStmt
        for i in range(len(ifthemStmt)):
            local_envi = [[]]
            local_envi = local_envi + c
            expr = self.visit(ast.ifthenStmt[i][0], c)
            if str(expr) == "TypeCannotBeInferred":
                raise TypeCannotBeInferred(ast)
            if str(expr) == "NoneType":
                if isinstance(ast.ifthenStmt[i][0], CallExpr): # if CallExp: need .method
                    setType(ast.ifthenStmt[i][0].method, c, BoolType)
                elif isinstance(ast.ifthenStmt[i][0], ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.ifthenStmt[i][0].arr, c, BoolType)
                else:
                    setType(ast.ifthenStmt[i][0], c, BoolType)
            elif str(expr) != "BooleanType":
                if str(expr) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInStatement(ast)
            for stmt in ast.ifthenStmt[i][1]: # list [Inst] 
                if isinstance(stmt, VarDecl):
                    local_envi[0].append(self.visit(stmt, local_envi))
                elif isinstance(stmt, ConstDecl):
                    local_envi[0].append(self.visit(stmt, local_envi))
                else:
                    self.visit(stmt, local_envi)
                    
        elStmt = ast.elseStmt
        if len(elStmt) !=0:
            local_envi = [[]] + c
            for stmt in elStmt:    
                if isinstance(stmt, VarDecl): 
                    local_envi[0].append(self.visit(stmt, local_envi))
                elif isinstance(stmt, ConstDecl):
                    local_envi[0].append(self.visit(stmt, local_envi))
                else:
                    self.visit(stmt, local_envi)

    # exp: Expr
    # sl: List[Inst]
    def visitWhile(self, ast, c):
        local_envi = [[]]
        local_envi = local_envi + c
        expr = self.visit(ast.exp, c)
        if str(expr) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        if str(expr) == "NoneType":
            if isinstance(ast.exp, CallExpr): # if CallExp: need .method
                setType(ast.exp.method, c, BoolType)
            elif isinstance(ast.exp, ArrayAccess): # if ArrayAccess: need .arr
                setTypeArrAccess(ast.exp.arr, c, BoolType)
            else:
                setType(ast.exp, c, BoolType)
        elif str(expr) != "BooleanType":
            if str(expr) == "Unknown":
                pass
            else:
                raise TypeMismatchInStatement(ast)
        for stmt in ast.sl:    
            if isinstance(stmt, VarDecl):
                local_envi[0].append(self.visit(stmt, local_envi))
            elif isinstance(stmt, ConstDecl):
                local_envi[0].append(self.visit(stmt, local_envi))
            else:
                self.visit(stmt, local_envi)

    # idx1: Id
    # expr: Expr
    # body: List[Inst]
    def visitForIn(self, ast, c):
        exp = self.visit(ast.expr, c)
        if str(exp) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        if str(exp) == "Unknown":
            pass
        if not isinstance(exp,ArrayType):
            raise TypeMismatchInStatement(ast)
        typ = NoneType()
        if isinstance(ast.expr, ArrayLiteral):
            if len(exp.dimen)>1:
                typ = ArrayType(exp.dimen[1:], exp.eletype)
            else:
                typ = exp.eletype
        else:
            for i in c: # get type idx1
                for elem in i:
                    if isinstance(ast.expr, Id):
                        if elem.name == ast.expr.name:
                            if len(elem.mtype.restype.dimen)>1:
                                typ = ArrayType(elem.mtype.restype.dimen[1:], elem.mtype.restype.eletype)
                            else:
                                typ = elem.mtype.restype.eletype
                            # raise TypeCannotBeInferred(typ)
                            
                    elif isinstance(ast.expr, CallExpr):
                        if elem.name == ast.expr.method.name:
                            if len(elem.mtype.restype.dimen)>1:
                                typ = ArrayType(elem.mtype.restype.dimen[1:], elem.mtype.restype.eletype)
                            else:
                                typ = elem.mtype.restype.eletype
                    elif isinstance(ast.expr, ArrayAccess):
                        if elem.name == ast.expr.arr.name:
                            if len(elem.mtype.restype.dimen)>1:
                                typ = ArrayType(elem.mtype.restype.dimen[1:], elem.mtype.restype.eletype)
                            else:
                                typ = elem.mtype.restype.eletype
        local_envi = [[Symbol(str(ast.idx1.name), MType([], typ))]]
        local_envi = local_envi + c
        for stmt in ast.body:    
            if isinstance(stmt, VarDecl):
                local_envi[0].append(self.visit(stmt, local_envi))                
            elif isinstance(stmt, ConstDecl):
                local_envi[0].append(self.visit(stmt, local_envi))
            else:
                self.visit(stmt, local_envi)

    # idx1: Id
    # expr: Expr
    # body: List[Inst]
    def visitForOf(self, ast, c):
        local_envi = [[Symbol(str(ast.idx1.name), MType([], NoneType()))]]
        local_envi = local_envi + c
        exp = self.visit(ast.expr, c)
        if str(exp) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        if str(exp) == "Unknown":
            pass
        elif str(exp) != "JSONType":
            raise TypeMismatchInStatement(ast)
        for stmt in ast.body:    
            if isinstance(stmt, VarDecl):
                local_envi[0].append(self.visit(stmt, local_envi))
                
            elif isinstance(stmt, ConstDecl):
                local_envi[0].append(self.visit(stmt, local_envi))
            else:
                self.visit(stmt, local_envi)
    def visitBreak(self, ast, c):pass
    def visitContinue(self, ast, c):pass

    # expr: Expr  # None if no expression
    def visitReturn(self, ast, c):
        if not ast.expr:
            return VoidType()
        else:
            return self.visit(ast.expr, c)
            
    # method: Id
    # param: List[Expr]
    def visitCallStmt(self, ast, c):

        param_lst = [self.visit(x,c) for x in ast.param]
        for i in c:
            for elem in i:
                if ast.method.name == elem.name: # Find the func name
                    if type(elem.mtype.restype) is not VoidType:
                        raise TypeMismatchInStatement(ast)
                    elif len(elem.mtype.intype) != len(param_lst):
                        raise TypeMismatchInStatement(ast)
                    else:
                        for i in range(len(param_lst)):
                            if isinstance(elem.mtype.intype[i], ArrayType) and not isinstance(param_lst[i], ArrayType):
                                raise TypeMismatchInExpression(ast)
                            elif not isinstance(elem.mtype.intype[i], ArrayType) and isinstance(param_lst[i], ArrayType):
                                raise TypeMismatchInExpression(ast)
                            elif isinstance(elem.mtype.intype[i], ArrayType) and isinstance(param_lst[i], ArrayType):
                                if(len(elem.mtype.intype[i]).intype) != len(param_lst[i].intype):
                                    raise TypeMismatchInStatement(ast)
                                else:
                                    pass
                            else:                         
                                if str(param_lst[i]) == "TypeCannotBeInferred":
                                    raise TypeCannotBeInferred(ast)
                                if str(elem.mtype.intype[i]) == 'NoneType' and str(param_lst[i]) =='NoneType':
                                    raise TypeCannotBeInferred(ast)
                                elif str(elem.mtype.intype[i]) == 'NoneType':
                                    elem.mtype.intype[i] = param_lst[i]
                                elif str(param_lst[i]) == 'NoneType':
                                    if isinstance(ast.param[i], CallExpr): # if CallExp: need .method
                                        setType(ast.param[i].method, c, type(elem.mtype.intype[i]))
                                    elif isinstance(ast.param[i], ArrayAccess): # if ArrayAccess: need .arr
                                        setTypeArrAccess(ast.param[i].arr, c, type(elem.mtype.intype[i]))
                                    else:
                                        setType(ast.param[i], c, type(elem.mtype.intype[i]))
                                elif str(elem.mtype.intype[i]) != str(param_lst[i]):       
                                    if str(elem.mtype.intype[i]) == "Unknown" or str(param_lst[i]) == "Unknown":
                                        pass
                                    else:
                                        raise TypeMismatchInStatement(ast)
                    return elem.mtype.restype
        raise Undeclared(Function(), ast.method.name)

    # method: Id
    # param: List[Expr]
    def visitCallExpr(self, ast, c):
        param_lst = [self.visit(x,c) for x in ast.param]
        for i in c:
            for elem in i:
                if ast.method.name == elem.name:
                    if len(elem.mtype.intype) != len(param_lst): # check length of param
                        raise TypeMismatchInExpression(ast)
                    else: # check Type of params
                        for i in range(len(param_lst)):
                            if isinstance(elem.mtype.intype[i], ArrayType) and not isinstance(param_lst[i], ArrayType):
                                raise TypeMismatchInExpression(ast)
                            elif not isinstance(elem.mtype.intype[i], ArrayType) and isinstance(param_lst[i], ArrayType):
                                raise TypeMismatchInExpression(ast)
                            elif isinstance(elem.mtype.intype[i], ArrayType) and isinstance(param_lst[i], ArrayType):
                                pass
                            else:
                                if str(param_lst[i]) == "TypeCannotBeInferred":
                                    return "TypeCannotBeInferred"
                                if str(elem.mtype.intype[i]) == 'NoneType' and str(param_lst[i]) =='NoneType':
                                    return "TypeCannotBeInferred"
                                elif str(elem.mtype.intype[i]) == 'NoneType':
                                    elem.mtype.intype[i] = param_lst[i]
                                elif str(param_lst[i]) == "NoneType":
                                    if isinstance(ast.param[i], CallExpr): # if CallExp: need .method
                                        setType(ast.param[i].method, c, type(elem.mtype.intype[i]))
                                    elif isinstance(ast.param[i], ArrayAccess): # if ArrayAccess: need .arr
                                        setType(ast.param[i].arr, c, type(elem.mtype.intype[i]))
                                    else:
                                        setType(ast.param[i], c, type(elem.mtype.intype[i]))
                                elif str(elem.mtype.intype[i]) != str(param_lst[i]):
                                    if str(elem.mtype.intype[i]) == "Unknown" or str(param_lst[i]) == "Unknown":
                                        pass
                                    else:
                                        raise TypeMismatchInExpression(ast)
                    return elem.mtype.restype
        raise Undeclared(Function(), ast.method.name)

    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast, c):
        op = ast.op
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)

        if str(left) == "TypeCannotBeInferred" or str(right) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        elemtyp = None
        rettyp = None
        if op in ['+', '-', '*', '/', '%']:
            elemtyp = NumberType
            rettyp = NumberType
        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            elemtyp = NumberType
            rettyp = BoolType
        elif op in ['==.']:
            elemtyp = StringType
            rettyp = BoolType
        elif op in ['&&', '||']:
            elemtyp = BoolType
            rettyp = BoolType
        elif op in [ '+.']:
            elemtyp = StringType
            rettyp = StringType
        if str(left) == "NoneType":
            if isinstance(ast.left, CallExpr): # if CallExp: need .method
                setType(ast.left.method, c, elemtyp)
            elif isinstance(ast.left, ArrayAccess): # if ArrayAccess: need .arr
                setTypeArrAccess(ast.left.arr, c, elemtyp)
            else:
                setType(ast.left, c, elemtyp)
            left = elemtyp()
        if str(right) == "NoneType":
            if isinstance(ast.right, CallExpr): # if CallExp: need .method
                setType(ast.right.method, c, elemtyp)
            elif isinstance(ast.right, ArrayAccess): # if ArrayAccess: need .arr
                setTypeArrAccess(ast.right.arr, c, elemtyp)
            else:
                setType(ast.right, c, elemtyp)
            right = elemtyp()
        if str(right) != str(elemtyp()) or str(left) != str(elemtyp()):
            if str(right) == "Unknown" or str(left) == "Unknown":
                pass
            else:
                raise TypeMismatchInExpression(ast)
        return rettyp()

    # op: str
    # body: Expr
    def visitUnaryOp(self, ast, c):
        op = ast.op
        expr = self.visit(ast.body, c)
        if str(expr) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        if op == '!':
            if str(expr) == "NoneType":
                if isinstance(ast.body, CallExpr): # if CallExp: need .method
                    setType(ast.body.method, c, BoolType)
                elif isinstance(ast.body, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.body.arr, c, BoolType)
                else:
                    setType(ast.body, c, BoolType)
            elif str(expr) == 'BooleanType':
                return BoolType()
            else:
                if str(expr) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            return BoolType()
            
        if op == '-':
            if str(expr) == "NoneType":
                if isinstance(ast.body, CallExpr): # if CallExp: need .method
                    setType(ast.body.method, c, NumberType)
                elif isinstance(ast.body, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.body.arr, c, NumberType)
                else:
                    setType(ast.body, c, NumberType)
            elif str(expr)=="NumberType":
                return NumberType()
            else:
                if str(expr) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            return NumberType()

    # name: str
    def visitId(self, ast, c):
        for elem in c:
            for i in elem:
                if ast.name == i.name:
                    return i.mtype.restype
        raise Undeclared(Identifier(), ast.name)

    # For access in Array
    # arr: Expr
    # idx: List[Expr]
    def visitArrayAccess(self, ast, c):
        arr_name = self.visit(ast.arr, c) # return type of Expr
        idx_lst =[ self.visit(elem, c) for elem in ast.idx] # list index         
        if str(arr_name) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)

        if not isinstance(arr_name, ArrayType):
            raise TypeMismatchInExpression(ast)
        for i in range(len(idx_lst)):
            if str(idx_lst[i]) == "TypeCannotBeInferred":
                raise TypeCannotBeInferred(ast)
            if str(idx_lst[i]) == "NoneType":
                if isinstance(ast.idx[i], Id):
                    setType(ast.idx[i].name, c, NumberType)
                elif isinstance(ast.arr, CallExpr):
                    setType(ast.idx[i].name, c, NumberType)
                    
            elif str(idx_lst[i]) != "NumberType":
                raise TypeMismatchInExpression(ast)
        lst = []
        typ = NoneType()
        find = False
        for i in c:
            for elem in i: # get Type and Size of array
                if isinstance(ast.arr, Id):
                    if elem.name == ast.arr.name:
                        typ = elem.mtype.restype.eletype
                        lst = elem.mtype.restype.dimen
                        find = True
                elif isinstance(ast.arr, CallExpr):
                    if elem.name == ast.arr.method.name:
                        typ = elem.mtype.restype.eletype
                        lst = elem.mtype.restype.dimen
                        find = True
                elif isinstance(ast.arr, ArrayAccess): # if ArrayAccess: need .arr
                    if elem.name == ast.arr.arr.name:
                        typ = elem.mtype.restype.eletype
                        lst = elem.mtype.restype.dimen
                        find = True
            if find:
                break
        if( len(lst) < len(ast.idx)):
            raise TypeMismatchInExpression(ast)
        if( len(lst) > len(ast.idx)):
            temp = len(lst) - len(ast.idx)
            return ArrayType(lst[temp:], typ)
        return typ

    # For access in JSON
    # json: Expr
    # idx: List[Expr]
    def visitJSONAccess(self, ast, c):
        json = self.visit(ast.json, c)
        idx_lst =[ self.visit(elem, c) for elem in ast.idx]
        
        if str(json) == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)
        if str(json) != "JSONType":
            raise TypeMismatchInExpression(ast)
        for idx in idx_lst:
            if str(idx) == "TypeCannotBeInferred":
                raise TypeCannotBeInferred(ast)
            if str(idx) != "StringType":
                raise TypeMismatchInExpression(ast)
        return Unknown()

    # value: number
    def visitNumberLiteral(self, ast, c):
        return NumberType()

    # value: bool
    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    # value: str
    def visitStringLiteral(self, ast, c):
        return StringType()

    # value: List[Literal]
    def visitArrayLiteral(self, ast, c):
        lst = ast.value
        dimen_lst = [len(lst)]
        elem_typ = self.visit(lst[0],c)
        temp = 0
        while isinstance(lst[0], ArrayLiteral):
            temp +=1
            dimen_lst+= [len(lst[0].value)]
            elem_typ = self.visit(lst[0].value[0],c)
            if isinstance(lst[0].value[0], ArrayLiteral):
                for i in lst[0].value:
                    if type(self.visit(i, c)) is not type(self.visit(lst[0].value[0], c)):
                        raise TypeMismatchInExpression(ast)
            else:
                for i in lst[0].value:
                    if str(self.visit(i, c)) is not str(self.visit(lst[0].value[0], c)):
                        raise TypeMismatchInExpression(ast)
            lst = lst[0].value
        return ArrayType(dimen_lst, elem_typ)

    # value: List[tuple]
    def visitJSONLiteral(self, ast, c):
        return JSONType()