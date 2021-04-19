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
class StaticCheck(Visitor):

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
