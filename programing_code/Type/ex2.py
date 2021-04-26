class Program: #decl:List[VarDecl],stmts:List[Stmt]
    pass
class VarDecl: #name:str
    pass
class Stmt(ABC): #abstract class
    pass
class Block(Stmt): #decl:List[VarDecl],stmts:List[Stmt]
    pass
class Assign(Stmt): #lhs:Id,rhs:Exp
    pass
class Exp(ABC): #abstract class
    pass
class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    pass
class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor
    pass
class IntLit(Exp): #val:int
    pass
class FloatLit(Exp): #val:float
    pass
class BoolLit(Exp): #val:bool
    pass
class Id(Exp): #name:str
    pass
def infer(id, o, typ):# hàm này để set kiểu 'typ' cho 'id'
    for x in o:
        if id.name == x[0]:
            x[1]= typ
class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o):
        o=[]
        for x in ctx.decl:
            o+= [self.visit(x,o)]
        for x in ctx.stmts: # ctx.stmts trả về một mảng các statement
            self.visit(x, o)
    def visitVarDecl(self, ctx: VarDecl, o):
        return [ctx.name, 0]

    def visitBlock(self,ctx:Block,o):
        for x in ctx.decl:
            o+= [self.visit(x,o)]
        for x in ctx.stmts:
            self.visit(x, o)

    def visitAssign(self, ctx: Assign, o):
        typ2 = self.visit(ctx.rhs, o) # nên đảo thứ tự typ1 và typ2, vì trong quá trình tính typ2 có thể tính ra được typ1, nếu tính typ1 trc nó sẽ chỉ là giá trị đầu [a, 0] như trong vardecl, và sẽ k thay đổi
        typ1 = self.visit(ctx.lhs, o)
        if typ1 ==0 and typ2 == 0:
            raise TypeCannotBeInferred(ctx)
        if typ1 == 0 and typ2!=0:
            infer(ctx.lhs, o, typ2)
            typ1 = typ2
        if typ1 != 0 and typ2== 0:
            infer(ctx.rhs, o, typ1)
            typ2 = typ1
        if typ1!=typ2:
            raise TypeMismatchInStatement(ctx)
    def visitBinOp(self, ctx: BinOp, o):
        typ1 = self.visit(ctx.e1, o)
        typ2 = self.visit(ctx.e2, o)
        if(ctx.op in ['+', '-', '*', '/']):
            if typ1 == 0:
                infer(ctx.e1,o,1)
                typ1 =1
            if typ2 ==0:
                infer(ctx.e2,o,1)
                typ2 =1
            if typ1 != 1 or typ2 != 1:
                raise TypeMismatchInExpression(ctx)
            return 1

        if(ctx.op in ['+.', '-.', '*.', '/.']):
            if typ1 ==0:
                infer(ctx.e1,o,2)
                typ1 = 2
            if typ2 ==0:
                infer(ctx.e2,o,2)
                typ2 =2
            if typ1 != 2 or typ2 != 2:
                raise TypeMismatchInExpression(ctx)
            return 2
        if ctx.op in ['=', '>']:
            if typ1 ==0:
                infer(ctx.e1,o,1)
                typ1 =1
            if typ2 ==0:
                infer(ctx.e2,o,1)
                typ2 =1
            if typ1 != 1 or typ2 != 1:
                raise TypeMismatchInExpression(ctx)
            return 3
        if ctx.op in ['=.', '>.']:
            if typ1 ==0:
                infer(ctx.e1,o,2)
                typ1 =2
            if typ2 ==0:
                infer(ctx.e2,o,2)
                typ2 =2
            if typ1 != 2 or typ2 != 2:
                raise TypeMismatchInExpression(ctx)
            return 3
        if ctx.op in ['!', '&&', '||', '>b', '=b']:
            if typ1 ==0:
                infer(ctx.e1,o,3)
                typ1 =3
            if typ2 ==0:
                infer(ctx.e2,o,3)
                typ2 =3
            if typ1 != 3 or typ2 != 3:
                raise TypeMismatchInExpression(ctx)
            return 3

    def visitUnOp(self, ctx: UnOp, o):
        typ = self.visit(ctx.e, o)
        if ctx.op == '-':
            if typ == 0:
                infer(ctx.e, o, 1)
                typ =1
            if typ != 1:
                raise TypeMismatchInExpression(ctx)
            return 1
        if ctx.op == '-.':
            if typ ==0:
                infer(ctx.e, o, 2)
                typ =2
            if typ != 2:
                raise TypeMismatchInExpression(ctx)
            return 2
        if ctx.op == '!':
            if typ ==0:
                infer(ctx.e, o, 3)
                typ =3
            if typ != 3:
                raise TypeMismatchInExpression(ctx)
            return 3
        if ctx.op == 'i2f':
            if typ ==0:
                infer(ctx.e, o, 1)
                typ =1
            if typ != 1:
                raise TypeMismatchInExpression(ctx)
            return 2
        if ctx.op == 'floor':
            if typ ==0:
                infer(ctx.e, o, 2)
                typ =2
            if typ != 2:
                raise TypeMismatchInExpression(ctx)
            return 1

    def visitIntLit(self, ctx: IntLit, o):
        return 1

    def visitFloatLit(self, ctx, o):
        return 2

    def visitBoolLit(self, ctx, o):
        return 3

    def visitId(self, ctx, o):
        for x in o:
            if x[0] == ctx.name:
                return x[1]
        raise UndeclaredIdentifier(ctx.name)
