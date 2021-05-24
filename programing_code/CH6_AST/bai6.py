from functools import reduce

# "a := b := 4"
# Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))

class ASTGeneration(MPVisitor):
    # program: exp EOF;
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return ctx.exp().accept(self)

    # exp: (term ASSIGN)* term;
    def visitExp(self, ctx: MPParser.ExpContext):
        if ctx.getChildCount() == 1:
            return ctx.term(0).accept(self)
        tmp = ctx.term()[::-1] # đảo ngược danh sách
        lst = list(zip(ctx.ASSIGN(), ctx.term()))
        lst = lst[::-1] # list này sẽ không có tmp(0) (là ctx.term term cuối)
        return reduce(lambda x, y: Binary(str(y[0]), y[1].accept(self), x), lst, tmp[0].accept(self))

    # term: factor COMPARE factor | factor;  vd: id(a) && id(b) == id(c)
    def visitTerm(self, ctx: MPParser.TermContext): 
        if ctx.getChildCount() == 1:
            return ctx.factor(0).accept(self)
        return Binary(str(ctx.COMPARE()), ctx.factor(0).accept(self), ctx.factor(1).accept(self))

    # factor: operand (ANDOR operand) *;    vd: id(a) && id(b) || id(c)
    def visitFactor(self, ctx: MPParser.FactorContext):
        if ctx.getChildCount() == 1:
            return ctx.operand(0).accept(self)
        lst = list(zip(ctx.ANDOR(), ctx.operand()[1:]))
        return reduce(lambda x, y: Binary(str(y[0]), x, y[1].accept(self)), lst, ctx.operand(0).accept(self))

    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(str(ctx.ID()))
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT())
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT())
        if ctx.exp():
            return self.visit(ctx.exp())