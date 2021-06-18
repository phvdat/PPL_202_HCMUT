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

    def setType(id, o, typ):
        for i in o:
            if id.name == i[0]:
                i.MType[1] = typ

    # decl: List[Decl]
    def visitProgram(self, ast, c):        
        c = c[:]
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
                # rettype = self.visit(x.returnType, None)
                # ===================RETURN trả VỀ CÁI GÌ THÌ HÀM SẼ LÀ TYPE ĐÓ =================================
                func = Symbol(x.name.name, MType([x.varType for x in x.param], Unknown))
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
        is_redeclare = self.lookup(ast.variable, c, lambda x: x.name)
        if is_redeclare:
            raise Redeclared(Variable(), ast.variable)
        
        lst = ast.varDimen
        if len(lst) >0:
            for i in lst:
                if(not isinstance(i, NumberType)):
                    raise TypeMismatchInStatement(ast)
        typ1 = self.visit(ast.typ, None)
        typ2 = self.visit(ast.varInit, None)

        if not ast.typ and not ast.varInit:
            return Symbol(ast.variable, MType(None, Unknown))
        elif ast.typ and not ast.varInit:
            return Symbol(ast.variable, MType(None, typ1))
        elif not ast.typ and ast.varInit:
            return Symbol(ast.variable, MType(None, typ2))
        elif isinstance(typ1, typ2):
            raise TypeMismatchInStatement(ast)


    # constant: Id
    # constDimen: List[Expr]       # empty list for scalar variable
    # typ: Type                   # NoneType if empty
    # constInit: Expr
    def visitConstDecl(self, ast, c):
        is_redeclare = self.lookup(ast.variable, c, lambda x: x.name)
        if is_redeclare:
            raise Redeclared(Variable(), ast.variable)
        
        lst = ast.varDimen
        if len(lst) >0:
            for i in lst:
                if(not isinstance(i, NumberType)):
                    raise TypeMismatchInStatement(ast)
        typ1 = self.visit(ast.typ, None)
        typ2 = self.visit(ast.varInit, None)
        if ast.typ and not isinstance(typ1, typ2):
            raise TypeMismatchInStatement(ast)
        return Symbol(ast.variable, MType(None, typ2))

    # name: Id
    # param: List[VarDecl]
    # body: List[Inst]
    def visitFuncDecl(self, ast, c): pass

    # lhs: LHS
    # rhs: Expr
    def visitAssign(self, ast, c): pass

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
            if isinstance(return_type, ArrayPointerType):

                if isinstance(rlt_expr, (ArrayPointerType, ArrayType)):
                    if not isinstance(rlt_expr.eleType, type(return_type.eleType)):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)

            elif isinstance(return_type, FloatType):
                if not isinstance(rlt_expr, (IntType, FloatType)):
                    raise TypeMismatchInStatement(ast)

            elif not isinstance(rlt_expr, type(return_type)):
                raise TypeMismatchInStatement(ast)
        return True # function have returned

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
            if isinstance(left, NumberType) and isinstance(right, Unknown):
                setType(ast.right, c, NumberType)
            elif isinstance(right, NumberType) and isinstance(left, Unknown):
                setType(ast.left, c, NumberType)
            else:
                raise TypeMismatchInExpression(ast)
            return NumberType()

        elif op in ['&&', '||']:
            if isinstance(left, BoolType) and isinstance(right, Unknown):
                setType(ast.right, c, BoolType)
            elif isinstance(right, BoolType) and isinstance(left, Unknown):
                setType(ast.left, c, BoolType)
            else:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in ['==.', '+.']:
            if isinstance(left, StringType) and isinstance(right, Unknown):
                setType(ast.right, c, StringType)
            elif isinstance(right, StringType) and isinstance(left, Unknown):
                setType(ast.left, c, StringType)
            else:
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
        is_declare = self.lookup(ast.name, c, lambda x: x.name)
        if not is_declare:
            raise Undeclared(Identifier(), ast.name)

        elif not is_declare.mtype.partype:
            return is_declare.mtype.rettype

        else:
            return None
        # for i in c:
        #     if ast.name == i[0]:
        #         return i.MType[1]
        # raise Undeclared(Identifier, ast.name)


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
            if not isinstance(idx, IntType):
                raise TypeMismatchInExpression(ast)
    # CHƯA BIẾT NÊN TRẢ RA CÁI GI =================================================================
        return arr

    # value: float
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
