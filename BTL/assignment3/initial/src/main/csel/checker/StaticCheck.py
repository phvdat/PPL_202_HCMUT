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
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass

class VoidType(Type):
    pass


class Unknown(Type):
    pass
    


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


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("read", MType([], StringType())),
            Symbol("print", MType([StringType()], VoidType())),
            Symbol("printSLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)
    # func set type

    def setType(id, c, typ):
        for i in c:
            if id.name == i.name:
                i.mtype.restype = typ

    # decl: List[Decl]
    def visitProgram(self, ast, c):
        c = [
            Symbol("read", MType([], StringType())),
            Symbol("print", MType([StringType()], VoidType())),
            Symbol("printSLn", MType([StringType()], VoidType()))]

        self.func_unused = []
        self.func_call_func = None
        # Check main function
        is_main = False
        for x in ast.decl:
            if isinstance(x, FuncDecl) and x.name.name == 'main':
                is_main = True
                break
        # Check Redeclare
        for x in ast.decl:
            if isinstance(x, VarDecl):
                c.append(self.visit(x, c))

            elif isinstance(x, ConstDecl):
                c.append(self.visit(x, c))

            elif isinstance(x, FuncDecl):
                func = Symbol(x.name.name, MType(self.visit(x, c), NoneType))
                for i in c:
                    if i.name == func.name:
                        raise Redeclared(Function(), func.name)

                c.append(func)

                if func.name != 'main':
                    self.func_unused.append(func)

        if not is_main:
            raise NoEntryPoint()

        for x in ast.decl:
            if isinstance(x, FuncDecl):
                self.func_call_func = x.name.name
                self.visit(x, c)

        if self.func_unused:
            raise UnreachableFunction(self.func_unused[0].name)
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
                if(not isinstance(i, NumberType)):
                    raise TypeMismatchInStatement(ast)
        
        vartype = ast.typ
        if ast.varInit:
            vInit = self.visit(ast.varInit, c)
        if (str(ast.typ) ==  'NoneType') and (ast.varInit is None):
            return Symbol(ast.variable.name, MType([], NoneType))
        elif (ast.varInit is None):
            return Symbol(ast.variable.name, MType([], vartype))
        elif (str(ast.typ) ==  'NoneType'):
            return Symbol(ast.variable.name, MType([], vInit))
        else:
            if str(type(vartype)) =="<class 'AST.StringType'>"  and str(type(vInit)) != "<class 'StaticCheck.StringType'>":
                raise TypeMismatchInStatement(ast)
            if str(type(vartype)) =="<class 'AST.NumberType'>"  and str(type(vInit)) != "<class 'StaticCheck.NumberType'>":
                raise TypeMismatchInStatement(ast)
            if str(type(vartype)) =="<class 'AST.BoolType'>"  and str(type(vInit)) != "<class 'StaticCheck.BoolType'>":
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
                if(not isinstance(i, NumberType)):
                    raise TypeMismatchInStatement(ast)
        
        vartype = ast.typ
        if ast.constInit:
            vInit = self.visit(ast.constInit, c)
        if (str(ast.typ) ==  'NoneType') and (ast.constInit is None):
            return Symbol(ast.constant.name, MType([], NoneType))
        elif (ast.constInit is None):
            return Symbol(ast.constant.name, MType([], vartype))
        elif (str(ast.typ) ==  'NoneType'):
            return Symbol(ast.constant.name, MType([], type(vInit)))
        else:
            if str(vartype) == 'NumberType':
                if not isinstance(vInit,NumberType):
                    raise TypeMismatchInStatement(ast)
            elif str(vartype) == 'StringType':
                if not isinstance(vInit,StringType):
                    raise TypeMismatchInStatement(ast)
            elif str(vartype) == 'BoolType':
                if not isinstance(vInit,BoolType):
                    raise TypeMismatchInStatement(ast)
                    
        return Symbol(ast.constant.name, MType([], vartype))
    # name: Id
    # param: List[VarDecl]
    # body: List[Inst]
    def visitFuncDecl(self, ast, c):
        local_envi = []
        para_list = []

        for param in ast.param:
            if param.variable in para_list:
                raise Redeclared(Parameter(), param.variable.name)

            else:
                para_list.append(param.variable)
                local_envi.append(self.visit(param, local_envi))
        temp = local_envi[:]
        
        for stmt in ast.body:    
            if isinstance(stmt, VarDecl):
                local_envi.append(self.visit(stmt, local_envi))

            elif isinstance(stmt, ConstDecl):
                local_envi.append(self.visit(stmt, local_envi))
            
            else:
                self.visit(stmt, local_envi + c)
        return [x.mtype.restype for x in temp]

    # lhs: LHS
    # rhs: Expr
    def visitAssign(self, ast, c):
        typ1=self.visit(ast.lhs,c)
        typ2=self.visit(ast.rhs,c)
        typ = [NumberType, StringType, BoolType]
        if type(typ2) not in typ and type(typ1) not in typ:
            raise TypeCannotBeInferred(type(typ2))
        # if not typ1 in [NumberType, StringType, BooleanType] and not typ2 in [NumberType, StringType, BooleanType]:
        #     raise TypeCannotBeInferred(type(typ2))
        # if not typ1 in [NumberType, StringType, BooleanType]:
        #     setType(ctx.lhs, o, typ2)
        #     typ1 = typ2
        # if not typ2 in [NumberType, StringType, BooleanType]:
        #     setType(ctx.rhs, o, typ1)
        #     typ2 = typ1
        # if typ1!=typ2:
        #     raise TypeMismatchInStatement(typ1)
        # return typ1
        raise TypeCannotBeInferred(type(typ2))

    # ifthenStmt: List[Tuple[Expr, List[Inst]]]
    # elseStmt: List[Inst]  # for Else branch, empty list if no Else
    def visitIf(self, ast, c): pass

    # exp: Expr
    # sl: List[Inst]
    def visitWhile(self, ast, c): pass

    # idx1: Id
    # expr: Expr
    # body: List[Inst]
    def visitFor(self, ast, c): pass

    def visitBreak(self, ast, c):
        if c[1] == False:
            raise BreakNotInLoop()

    def visitContinue(self, ast, c):
        if c[1] == False:
            raise ContinueNotInLoop()

    # expr: Expr  # None if no expression
    def visitReturn(self, ast, c):
        return_type = c[-1]
        if not ast.expr:
            if not isinstance(return_type, VoidType):
                raise TypeMismatchInStatement(ast)

        elif isinstance(return_type, VoidType):
            raise TypeMismatchInStatement(ast)

        else:
            envi = c[0]
            rlt_expr = self.visit(ast.expr, envi)
            if isinstance(rlt_expr, ArrayType):
                if not isinstance(rlt_expr.eleType, type(return_type.eleType)):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)

            if isinstance(return_type, NumberType):
                if not isinstance(rlt_expr, NumberType):
                    raise TypeMismatchInStatement(ast)

            elif not isinstance(rlt_expr, type(return_type)):
                raise TypeMismatchInStatement(ast)
        return True  # function have returned

    # method: Id
    # param: List[Expr]
    def visitCallExpr(self, ast, c): pass

    # method: Id
    # param: List[Expr]
    def visitCallStmt(self, ast, c): pass

    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast, c):
        op = ast.op
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)

        if op in ['+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=']:
            if isinstance(left, NumberType) and isinstance(right, NoneType):
                setType(ast.right, c, NumberType)
            elif isinstance(right, NumberType) and isinstance(left, NoneType):
                setType(ast.left, c, NumberType)
            elif not isinstance(left, type(right)):
                raise TypeMismatchInExpression(right)
            return NumberType()

        elif op in ['&&', '||']:
            if isinstance(left, BoolType) and isinstance(right, NoneType):
                setType(ast.right, c, BoolType)
            elif isinstance(right, BoolType) and isinstance(left, NoneType):
                setType(ast.left, c, BoolType)
            elif not isinstance(left, type(right)):
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in ['==.', '+.']:
            if isinstance(left, StringType) and isinstance(right, NoneType):
                setType(ast.right, c, StringType)
            elif isinstance(right, StringType) and isinstance(left, NoneType):
                setType(ast.left, c, StringType)
            elif not isinstance(left, type(right)):
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
        idx = [self.visit(ast.idx, c) for idx in ast.idx]

        if not isinstance(arr, ArrayType):
            raise TypeMismatchInExpression(ast)
        for idx in idx:
            if not isinstance(idx, IntType):
                raise TypeMismatchInExpression(ast)
    # CHƯA BIẾT NÊN TRẢ RA CÁI GI =================================================================
        return arr

    # For access in JSON
    # json: Expr
    # idx: List[Expr]
    def visitJSONAccess(self, ast, c):
        json = self.visit(ast.json, c)
        idx = [self.visit(ast.idx, c) for idx in ast.idx]

        if not isinstance(json, ArrayType):
            raise TypeMismatchInExpression(ast)
        for idx in idx:
            if not isinstance(idx, NumberType):
                raise TypeMismatchInExpression(ast)
    # CHƯA BIẾT NÊN TRẢ RA CÁI GI =================================================================
        return arr

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
        return ArrayType()

    # value: List[tuple]
    def visitJSONLiteral(self, ast, c):
        return JSONType()
