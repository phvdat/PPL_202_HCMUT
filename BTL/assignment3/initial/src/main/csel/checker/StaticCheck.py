# Pham Van Dat
# 181192
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
calledFunc = []

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
                if(not isinstance(self.visit(i, c), NumberType)):
                    raise TypeMismatchInExpression(ast)

        vartype = ast.typ
        if ast.varInit:
            vInit = self.visit(ast.varInit, c)
        # =======================ARRAY========================
        if lst: # if array declare
            if ast.varInit:
                if not isinstance(vInit,ArrayType):     # if rhs not array type
                    raise TypeMismatchInStatement(ast)
            if isinstance(vartype, ArrayType):      # if type elem = arraytype => false
                raise TypeMismatchInStatement(ast)
            return Symbol(ast.variable.name, MType([], ArrayType(lst,vartype)))
        
        # =======================JSON========================
        if ast.varInit:
            if str(vInit) == str(JSONType()):
                if str(vartype) != "NoneType":
                    raise TypeMismatchInStatement(ast)
                return Symbol(ast.variable.name, MType([], JSONType()))


        # ==============NUMBER, STRING, BOOLEAN===============
        if (str(vartype) ==  'NoneType') and (ast.varInit is None):
            return Symbol(ast.variable.name, MType([], NoneType()))
        elif (ast.varInit is None):
            return Symbol(ast.variable.name, MType([], vartype))
        elif (str(vartype) ==  'NoneType'):
            return Symbol(ast.variable.name, MType([], vInit))
        elif str(vartype) != str(vInit):
            raise TypeMismatchInStatement(ast)
        # elif not issubclass(type(vInit), type(vartype)):
        #     raise TypeMismatchInStatement(ast)

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
                raise TypeMismatchInStatement(ast)
            if isinstance(vartype, ArrayType):      # if type elem = arraytype => false
                raise TypeMismatchInStatement(ast)
            return Symbol(ast.variable.name, MType([], ArrayType(lst,vartype)))



        # =======================JSON========================
        if ast.constInit:
            if str(vInit) == str(JSONType()):
                if str(vartype) != "NoneType":
                    raise TypeMismatchInStatement(ast)
                return Symbol(ast.variable.name, MType([], JSONType()))


        # ==============NUMBER, STRING, BOOLEAN===============
        if (str(ast.typ) ==  'NoneType') and (ast.constInit is None):
            return Symbol(ast.constant.name, MType([], NoneType()))
        elif (ast.constInit is None):
            return Symbol(ast.constant.name, MType([], vartype))
        elif (str(ast.typ) ==  'NoneType'):
            return Symbol(ast.constant.name, MType([], vInit))
        elif vartype != vInit:
            raise TypeMismatchInStatement(ast)
        
        return Symbol(ast.constant.name, MType([], vartype))

    # name: Id
    # param: List[VarDecl]
    # body: List[Inst]
    def visitFuncDecl(self, ast, c):
        
        local_envi = []
        para_list = []
        return_typ = None
        for param in ast.param:
            if param.variable.name in para_list:
                raise Redeclared(Parameter(), param.variable.name)

            else:
                para_list.append(param.variable.name)
                local_envi.append(self.visit(param, local_envi))
        
        rt_param_lst = local_envi
        local_envi_c = local_envi + c

        for stmt in ast.body:    
            if isinstance(stmt, VarDecl):
                local_envi_c.append(self.visit(stmt, local_envi))
                local_envi.append(self.visit(stmt, local_envi))
                
            elif isinstance(stmt, ConstDecl):
                local_envi_c.append(self.visit(stmt, local_envi))
                local_envi.append(self.visit(stmt, local_envi))
            else:

                if isinstance(stmt, Return):
                    return_typ = self.visit(stmt, local_envi_c)
                else:
                    self.visit(stmt, local_envi_c)

        return [x.mtype.restype for x in rt_param_lst] , return_typ

        # temp=[i.name for i in local_envi]    # mảng các tên biến trong block
        # for x in c:
        #     if x.name not in temp: # tim biến  thuộc o k dc khai báo trong block
        #         for y in local_envi_c:
        #             if x.name==y.name: # mà dc sử dụng trong block
        #                 c.remove(x)
        #                 c.append(y)

    # lhs: LHS
    # rhs: Expr
    def visitAssign(self, ast, c):

        typ2=self.visit(ast.rhs,c)
        typ1=self.visit(ast.lhs,c)
        if type(typ1) is VoidType or type(typ2) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(typ1) is ArrayType or type(typ1) is JSONType:
            pass
        else:
            if type(typ2) is NoneType and type(typ1) is NoneType:
                raise TypeCannotBeInferred(ast)
            if type(typ1) is NoneType:
                setType(ast.lhs, c, type(typ2))
                typ1 = typ2
            if type(typ2) is NoneType:
                setType(ast.rhs, c, type(typ1))
                typ2 = typ1
            if str(typ1) != str(typ2):
                raise TypeMismatchInStatement(ast)
    # ifthenStmt: List[Tuple[Expr, List[Inst]]]
    # elseStmt: List[Inst]  # for Else branch, empty list if no Else
    def visitIf(self, ast, c):
        local_envi = []
        ifthemStmt = ast.ifthenStmt
        # for ifthen in ifthemStmt:
            

    # exp: Expr
    # sl: List[Inst]
    def visitWhile(self, ast, c): pass

    # idx1: Id
    # expr: Expr
    # body: List[Inst]
    def visitFor(self, ast, c): pass

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
        # raise TypeMismatchInExpression(param_lst)

        for elem in c:
            if ast.method.name == elem.name:
                if type(elem.mtype.restype) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                elif len(elem.mtype.intype) != len(param_lst):
                    raise TypeMismatchInStatement(ast)
                
                else:
                    for i in range(len(param_lst)):
                        if str(elem.mtype.intype[i]) == 'NoneType' and str(param_lst[i]) =='NoneType':
                            raise TypeMismatchInStatement(ast)
                        elif str(elem.mtype.intype[i]) == 'NoneType':
                            elem.mtype.intype[i] = param_lst[i]
                        elif str(param_lst[i]) == 'NoneType':
                            setType(ast.param[i], c, type(elem.mtype.intype[i]))
                        elif str(elem.mtype.intype[i]) != str(param_lst[i]):
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
                            setType(ast.param[i], c, type(elem.mtype.intype[i]))
                        elif str(elem.mtype.intype[i]) != str(param_lst[i]):
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

        if op in ['+', '-', '*', '/', '%']:
            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr):
                    setType(ast.left.method, c, NumberType)
                else:
                    setType(ast.left, c, NumberType)
                left = NumberType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr):
                    setType(ast.right.method, c, NumberType)
                else:
                    setType(ast.right, c, NumberType)
                right = NumberType()
            if not isinstance(right, NumberType) or not isinstance(left, NumberType):
                raise TypeMismatchInExpression(ast)
            return NumberType()
        
        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr):
                    setType(ast.left.method, c, NumberType)
                else:
                    setType(ast.left, c, NumberType)
                left = NumberType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr):
                    setType(ast.right.method, c, NumberType)
                else:
                    setType(ast.right, c, NumberType)
                right = NumberType()
            if not isinstance(right, NumberType) or not isinstance(left, NoneType):
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in ['==.']:
            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr):
                    setType(ast.left.method, c, StringType)
                else:
                    setType(ast.left, c, StringType)
                left = StringType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr):
                    setType(ast.right.method, c, StringType)
                else:
                    setType(ast.right, c, StringType)
                right = StringType()
            if not isinstance(right, StringType) or not isinstance(left, NoneType):
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in ['&&', '||']:
            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr):
                    setType(ast.left.method, c, BoolType)
                else:
                    setType(ast.left, c, BoolType)
                left = BoolType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr):
                    setType(ast.right.method, c, BoolType)
                else:
                    setType(ast.right, c, BoolType)
                right = BoolType()
            if not isinstance(right, BoolType) or not isinstance(left, NoneType):
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in [ '+.']:
            if isinstance(left, NoneType):
                if isinstance(ast.left, CallExpr):
                    setType(ast.left.method, c, StringType)
                else:
                    setType(ast.left, c, StringType)
                left = StringType()
            if isinstance(right, NoneType):
                if isinstance(ast.right, CallExpr):
                    setType(ast.right.method, c, StringType)
                else:
                    setType(ast.right, c, StringType)
                right = StringType()
            if not isinstance(right, StringType) or not isinstance(left, NoneType):
                raise TypeMismatchInExpression(ast)
            return StringType()

    # op: str
    # body: Expr
    def visitUnaryOp(self, ast, c):
        op = ast.op
        expr = self.visit(ast.body, c)

        if op == '!':
            if isinstance(expr, BoolType):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        if op == '-':
            if isinstance(expr, NumberType):
                return NumberType()
            else:
                raise TypeMismatchInExpression(ast)

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
        arr = self.visit(ast.arr, c)
        idx_lst =[ self.visit(elem, c) for elem in ast.idx]
        
        if not isinstance(arr, ArrayType):
            raise TypeMismatchInExpression(ast)
        for idx in idx_lst:
            if not isinstance(idx, NumberType):
                raise TypeMismatchInExpression(ast)
        return arr

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
        return json

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
        return ArrayType([x.value for x in ast.value], self.visit(ast.value[0], c))

    # value: List[tuple]
    def visitJSONLiteral(self, ast, c):
        return JSONType()
