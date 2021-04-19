class Program: #decl:List[VarDecl],exp:Exp
    pass
class VarDecl: #name:str,typ:Type
    pass
class Type(ABC): #abstract class
    pass
class IntType(Type):
    pass
class FloatType(Type):
    pass
class BoolType(Type):
    pass
class Exp(ABC): #abstract class
    pass
class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
    pass
class UnOp(Exp): #op:str,e:Exp #op is -, !
    pass
class IntLit(Exp): #val:int
    pass
class FloatLit(Exp): #val:float
    pass
class BoolLit(Exp): #val:bool
    pass
class Id(Exp): #name:str
    pass

class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o):
        return self.visit(ctx.exp, ctx.decl)
    def visitVarDecl(self,ctx:VarDecl,o):
        return [ctx]
    def visitBinOp(self,ctx:BinOp,o):
        typ1 = self.visit(ctx.e1,o)
        typ2 = self.visit(ctx.e2,o)
            
        if ctx.op in ['+','-','*'] :
            if typ1 ==3 or typ2 == 3:
                raise TypeMismatchInExpression(ctx)
            if typ1!=typ2 or ctx.op =='/':
                return 2
            return typ1
        if ctx.op == '/' :
            if typ1 ==3 or typ2 == 3:
                raise TypeMismatchInExpression(ctx)
            return 2
        if ctx.op in ['!', '&&', '||' ]:
            if typ1 !=3 or typ2 != 3:
                raise TypeMismatchInExpression(ctx)
            return typ1
        if ctx.op in ['>', '<', '==','!=']:
            if typ1 != typ2:
                raise TypeMismatchInExpression(ctx)
            return 3

    def visitUnOp(self,ctx:UnOp,o):
        typ = self.visit(ctx.e,o)
        if ctx.op == '-':
            if typ == 3:
                raise TypeMismatchInExpression(ctx)
            return typ
        if ctx.op =='!':
            if typ == 1 or typ == 2:
                raise TypeMismatchInExpression(ctx)
            return typ

    def visitIntLit(self,ctx:IntLit,o):
        return 1

    def visitFloatLit(self,ctx,o):
        return 2

    def visitBoolLit(self,ctx,o):
        return 3

    def visitId(self,ctx,o):
        for decl in o:
                if decl == ctx.name:
                    typ = decl.tye
                    if type(typ) is IntType():
                        return 1
                    if type(typ) is FloatType():
                        return 2
                    if type(typ) is BoolType():
                        return 3
        raise UndeclaredIdentifier(ctx.name)

    # def visitIntLit(self,ctx:IntLit,o):
    #     return IntType()

    # def visitFloatLit(self,ctx,o):
    #     return FloatType()

    # def visitBoolLit(self,ctx,o):
    #     return FloatType()