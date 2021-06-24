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
    for i in c:
        if id.name == i.name:
            i.mtype.restype = typ()
            break
def setTypeArrAccess(id, c, typ):
    for i in c:
        if id.name == i.name:
            i.mtype.restype.eletype = typ()
            break

class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [

            Symbol("read", MType([], StringType())),
            Symbol("print", MType([StringType()], VoidType())),
            Symbol("printSLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    # decl: List[Decl]
    def visitProgram(self, ast, c):
        c = self.global_envi[:]
        
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
                c.append(self.visit(x, c))

            elif isinstance(x, ConstDecl):
                c.append(self.visit(x, c))

            elif isinstance(x, FuncDecl):
                lst_typ, return_typ = self.visit(x, c)
                func = Symbol(x.name.name, MType(lst_typ, return_typ))
                for i in c:
                    if i.name == func.name:
                        raise Redeclared(Function(), func.name)
                c.append(func)


    # variable: Id
    # varDimen: List[Expr]     # empty list for scalar variable
    # typ: Type               # NoneType if empty
    # varInit: Expr           # None if no initial
    def visitVarDecl(self, ast, c):
        for i in c:
            if i.name == ast.variable.name:
                raise Redeclared(Variable(), ast.variable.name)
        lst = ast.varDimen
        if lst:
            for i in lst:
                if isinstance(self.visit(i, c), NoneType):
                    raise TypeCannotBeInferred(ast)
                if(not isinstance(self.visit(i, c), NumberType)):
                    raise TypeMismatchInExpression(ast)

        vartype = ast.typ
        if ast.varInit:
            vInit = self.visit(ast.varInit, c)
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
        for i in c:
            if i.name == ast.constant.name:
                raise Redeclared(Constant(), ast.constant.name)
        lst = ast.constDimen
        if lst:
            for i in lst:
                if(not isinstance(self.visit(i, c), NumberType)):
                    raise TypeMismatchInStatement(ast)
        
        vartype = ast.typ
        vInit = self.visit(ast.constInit, c)
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
            return Symbol(ast.variable.name, MType([], ArrayType(lst,vartype)))
        # =======================JSON========================
        if ast.constInit:
            if str(vInit) == "JSONType":
                if str(vartype) != "NoneType":
                    raise TypeMismatchInStatement(ast)
                return Symbol(ast.variable.name, MType([], JSONType()))
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
        local_envi = []
        para_list = [] # use to check param có bị trùng
        return_typ = NoneType()
        for param in ast.param:
            if param.variable.name in para_list:
                raise Redeclared(Parameter(), param.variable.name)

            else:
                para_list.append(param.variable.name)
                local_envi.append(self.visit(param, local_envi))
                # if isinstance(param, ArrayAccess)
        
        rt_param_lst = local_envi[:]

        for stmt in ast.body:    
            if isinstance(stmt, VarDecl):
                local_envi.append(self.visit(stmt, local_envi))
                
            elif isinstance(stmt, ConstDecl):
                local_envi.append(self.visit(stmt, local_envi))
            else:

                if isinstance(stmt, Return):
                    return_typ = self.visit(stmt, local_envi + c)
                else:
                    self.visit(stmt, local_envi + c)
        return [x.mtype.restype for x in rt_param_lst] , return_typ

    # lhs: LHS
    # rhs: Expr
    def visitAssign(self, ast, c):
        typ2=self.visit(ast.rhs,c)
        typ1=self.visit(ast.lhs,c)
        if type(typ1) is VoidType or type(typ2) is VoidType:
            raise TypeMismatchInStatement(ast)
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
                if str(typ1) == "Unknown" or str(typ2) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInStatement(ast)
    # ifthenStmt: List[Tuple[Expr, List[Inst]]]
    # elseStmt: List[Inst]  # for Else branch, empty list if no Else
    def visitIf(self, ast, c):
        ifthemStmt = ast.ifthenStmt
        for elem in ifthemStmt:
            local_envi = []
            exp = self.visit(elem[0], c)
            if str(exp) != "BooleanType":
                raise TypeMismatchInStatement(ast)

            for stmt in elem[1]:    
                if isinstance(stmt, VarDecl):
                    local_envi.append(self.visit(stmt, local_envi))      
                elif isinstance(stmt, ConstDecl):
                    local_envi.append(self.visit(stmt, local_envi))
                else:
                    self.visit(stmt, local_envi + c)

        elStmt = ast.elseStmt
        if len(elStmt) !=0:
            local_envi = []
            for stmt in elStmt:    
                if isinstance(stmt, VarDecl):
                    local_envi.append(self.visit(stmt, local_envi))
                elif isinstance(stmt, ConstDecl):
                    local_envi.append(self.visit(stmt, local_envi))
                else:
                    self.visit(stmt, local_envi + c)



    # exp: Expr
    # sl: List[Inst]
    def visitWhile(self, ast, c):
        
        local_envi = []
        exp = self.visit(ast.exp, c)
        if str(exp) != "BooleanType":
            raise TypeMismatchInStatement(ast)

        for stmt in ast.sl:    
            if isinstance(stmt, VarDecl):
                local_envi.append(self.visit(stmt, local_envi))
                
            elif isinstance(stmt, ConstDecl):
                local_envi.append(self.visit(stmt, local_envi))
            else:
                self.visit(stmt, local_envi + c)

    # idx1: Id
    # expr: Expr
    # body: List[Inst]
    def visitForIn(self, ast, c):

        exp = self.visit(ast.expr, c)
        if not isinstance(exp,ArrayType):
            raise TypeMismatchInStatement(ast)

        typ = NoneType()
        for elem in c:
            if isinstance(ast.expr, Id):
                if elem.name == ast.expr.name:
                    typ = elem.mtype.restype.eletype
            elif isinstance(ast.expr, CallExpr):
                if elem.name == ast.expr.method.name:
                    typ = elem.mtype.restype.eletype
            elif isinstance(ast.expr, ArrayAccess): # if ArrayAccess: need .arr
                if elem.name == ast.expr.arr.name:
                    typ = elem.mtype.restype.eletype
        local_envi = [Symbol(str(ast.idx1.name), MType([], typ))]

        for stmt in ast.body:    
            if isinstance(stmt, VarDecl):
                local_envi.append(self.visit(stmt, local_envi))
                
            elif isinstance(stmt, ConstDecl):
                local_envi.append(self.visit(stmt, local_envi))
            else:
                self.visit(stmt, local_envi + c)

    # idx1: Id
    # expr: Expr
    # body: List[Inst]
    def visitForOf(self, ast, c):
        local_envi = [Symbol(str(ast.idx1.name), MType([], NoneType()))]

        exp = self.visit(ast.expr, c)
        if not isinstance(exp,JSONType):
            raise TypeMismatchInStatement(ast)

        for stmt in ast.body:    
            if isinstance(stmt, VarDecl):
                local_envi.append(self.visit(stmt, local_envi))
                
            elif isinstance(stmt, ConstDecl):
                local_envi.append(self.visit(stmt, local_envi))
            else:
                self.visit(stmt, local_envi + c)

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

        for elem in c:
            if ast.method.name == elem.name: # Find the func name
                if type(elem.mtype.restype) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                elif len(elem.mtype.intype) != len(param_lst):
                    raise TypeMismatchInStatement(ast)
                
                else:
                    for i in range(len(param_lst)):
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

        for elem in c:

            if ast.method.name == elem.name:
                if len(elem.mtype.intype) != len(param_lst):
                    raise TypeMismatchInExpression(ast)
                
                else:

                    for i in range(len(param_lst)):
                        if str(elem.mtype.intype[i]) == 'NoneType' and str(param_lst[i]) =='NoneType':
                            raise TypeMismatchInExpression(ast)
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
        # elif op in ['+', '-', '*', '/', '%']:
        if op in ['+', '-', '*', '/', '%']:
            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr): # if CallExp: need .method
                    setType(ast.left.method, c, NumberType)
                elif isinstance(ast.left, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.left.arr, c, NumberType)
                else:
                    setType(ast.left, c, NumberType)
                left = NumberType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr): # if CallExp: need .method
                    setType(ast.right.method, c, NumberType)
                elif isinstance(ast.right, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.right.arr, c, NumberType)
                else:
                    setType(ast.right, c, NumberType)
                right = NumberType()
            if not isinstance(right, NumberType) or not isinstance(left, NumberType):
                if str(right) == "Unknown" or str(left) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            return NumberType()
        
        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr): # if CallExp: need .method
                    setType(ast.left.method, c, NumberType)
                elif isinstance(ast.left, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.left.arr, c, NumberType)
                else:
                    setType(ast.left, c, NumberType)
                left = NumberType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr): # if CallExp: need .method
                    setType(ast.right.method, c, NumberType)
                elif isinstance(ast.right, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.right.arr, c, NumberType)
                else:
                    setType(ast.right, c, NumberType)
                right = NumberType()
            if not isinstance(right, NumberType) or not isinstance(left, NumberType):
                if str(right) == "Unknown" or str(left) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in ['==.']:
            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr): # if CallExp: need .method
                    setType(ast.left.method, c, StringType)
                elif isinstance(ast.left, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.left.arr, c, StringType)
                else:
                    setType(ast.left, c, StringType)
                left = StringType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr): # if CallExp: need .method
                    setType(ast.right.method, c, StringType)
                elif isinstance(ast.right, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.right.arr, c, StringType)
                else:
                    setType(ast.right, c, StringType)
                right = StringType()
            if not isinstance(right, StringType) or not isinstance(left, StringType):
                if str(right) == "Unknown" or str(left) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in ['&&', '||']:
            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr): # if CallExp: need .method
                    setType(ast.left.method, c, BoolType)
                elif isinstance(ast.left, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.left.arr, c, BoolType)
                else:
                    setType(ast.left, c, BoolType)
                left = BoolType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr): # if CallExp: need .method
                    setType(ast.right.method, c, BoolType)
                elif isinstance(ast.right, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.right.arr, c, BoolType)
                else:
                    setType(ast.right, c, BoolType)
                right = BoolType()
            if str(right) != "BooleanType" or str(left) != "BooleanType":
                if str(right) == "Unknown" or str(left) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in [ '+.']:

            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr): # if CallExp: need .method
                    setType(ast.left.method, c, StringType)
                elif isinstance(ast.left, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.left.arr, c, StringType)
                else:
                    setType(ast.left, c, StringType)
                left = StringType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr): # if CallExp: need .method
                    setType(ast.right.method, c, StringType)
                elif isinstance(ast.right, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.right.arr, c, StringType)
                else:
                    setType(ast.right, c, StringType)
                right = StringType()
            if str(right) != "StringType" or str(left) != "StringType":
                if str(right) == "Unknown" or str(left) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            return StringType()

    # op: str
    # body: Expr
    def visitUnaryOp(self, ast, c):
        op = ast.op
        expr = self.visit(ast.body, c)

        if op == '!':
            if isinstance(expr, NoneType):
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
            if isinstance(expr, NoneType):
                if isinstance(ast.body, CallExpr): # if CallExp: need .method
                    setType(ast.body.method, c, NumberType)
                elif isinstance(ast.body, ArrayAccess): # if ArrayAccess: need .arr
                    setTypeArrAccess(ast.body.arr, c, NumberType)
                else:
                    setType(ast.body, c, NumberType)
            elif isinstance(expr, NumberType):
                return NumberType()
            else:
                if str(expr) == "Unknown":
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            return NumberType()

    # name: str
    def visitId(self, ast, c):
        for i in c:
            if ast.name == i.name:
                return i.mtype.restype
        raise Undeclared(Identifier(), ast.name)

    # For access in Array
    # arr: Expr
    # idx: List[Expr]
    def visitArrayAccess(self, ast, c):
        arr_name = self.visit(ast.arr, c) # return type of Expr
        idx_lst =[ self.visit(elem, c) for elem in ast.idx] # list index
        
        if not isinstance(arr_name, ArrayType):
            raise TypeMismatchInExpression(ast)
        for i in range(len(idx_lst)):
            if str(idx_lst[i]) == "NoneType":
                if isinstance(ast.idx[i], Id):
                    setType(ast.idx[i].name, c, NumberType)
                elif isinstance(ast.arr, CallExpr):
                    setType(ast.idx[i].name, c, NumberType)
                    
            elif str(idx_lst[i]) != "NumberType":
                raise TypeMismatchInExpression(ast)


        len_idx = 0
        typ = NoneType()
        for elem in c: # get Type and Size of array
            if isinstance(ast.arr, Id):
                if elem.name == ast.arr.name:
                    typ = elem.mtype.restype.eletype
                    len_idx = len(elem.mtype.restype.dimen)
            elif isinstance(ast.arr, CallExpr):
                if elem.name == ast.arr.method.name:
                    typ = elem.mtype.restype.eletype
                    len_idx = len(elem.mtype.restype.dimen)
            elif isinstance(ast.arr, ArrayAccess): # if ArrayAccess: need .arr
                if elem.name == ast.arr.arr.name:
                    typ = elem.mtype.restype.eletype
                    len_idx = len(elem.mtype.restype.dimen)

        if( len_idx < len(ast.idx)):
            raise TypeMismatchInExpression(ast)
        return typ
        # return arr

    # For access in JSON
    # json: Expr
    # idx: List[Expr]
    def visitJSONAccess(self, ast, c):
        json = self.visit(ast.json, c)
        idx_lst =[ self.visit(elem, c) for elem in ast.idx]
        
        if not isinstance(json, JSONType):
            raise TypeMismatchInExpression(ast)
        for idx in idx_lst:
            if not isinstance(idx, StringType):
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
        for elem in lst:
            if str(self.visit(elem, c)) !=  str(self.visit(lst[0], c)):
                raise TypeMismatchInExpression(ast)
                
        return ArrayType([x for x in lst], self.visit(lst[0], c))

    # value: List[tuple]
    def visitJSONLiteral(self, ast, c):
        return JSONType()
