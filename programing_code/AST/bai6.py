# program: exp EOF;

# exp: (term ASSIGN)* term;

# term: factor COMPARE factor | factor;

# factor: operand (ANDOR operand)*; 

# operand: ID | INTLIT | BOOLIT | '(' exp ')';

# INTLIT: [0-9]+ ;

# BOOLIT: 'True' | 'False' ;

# ANDOR: 'and' | 'or' ;

# ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

# COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

# ID: [a-z]+ ;

# and AST classes as follows:

class Expr(ABC):pass

class Binary(Expr):  #op:string;left:Expr;right:Expr
    pass
class Id(Expr): #value:string
    pass
class IntLiteral(Expr): #value:int
    pass
class BooleanLiteral(Expr): #value:boolean
    pass
# Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?



# "a := b := 4" => Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))
# class ASTGeneration(MPVisitor):
#     # program: exp EOF;
#     def visitProgram(self,ctx:MPParser.ProgramContext):
#         return Expr(self.visit(ctx.exp()))

#     # exp: (term ASSIGN)* term;
#     def visitExp(self,ctx:MPParser.ExpContext):
#         assignlist = ctx.ASSIGN()
#         return [Binary(assignlist(0).getText(), i) for i in ctx.term]


#     # term: factor COMPARE factor | factor;
#     def visitTerm(self,ctx:MPParser.TermContext): 
#         if ctx.getChildCount() == 3:
#             return self.visit(ctx.COMPARE()) + self.visit(ctx.factor(0)) + self.visit(ctx.factor(1))
#         else:
#             return self.visit(ctx.factor())

#     # factor: operand (ANDOR operand)*; 
#     def visitFactor(self,ctx:MPParser.FactorContext):
#         operandlist = ctx.operand()
#         andorlist = ctx.ANDOR()
#         return [Binary(andorlist(0).getText(), oper) for oper in operandlist]
#     # operand: ID | INTLIT | BOOLIT | '(' exp ')';
#     def visitOperand(self,ctx:MPParser.OperandContext):
#         if(ctx.ID()):
#             return Id(ctx.ID().getText())
#         elif ctx.INTLIT():
#             return IntLiteral(ctx.INTLIT().getText())
#         elif ctx.BOOLIT():
#             return BooleanLiteral(ctx.BOOLIT().getText())
#         else:
#             return self.visit(ctx.exp())



class ASTGeneration(MPVisitor):
    # program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Expr(self.visit(ctx.exp()))

    # exp: (term ASSIGN)* term;
    def visitExp(self,ctx:MPParser.ExpContext):
        assignlist = ctx.ASSIGN()
        return [Binary(assignlist(0).getText(), i) for i in ctx.term]


    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.getChildCount() == 3:
            return self.visit(ctx.COMPARE()) + self.visit(ctx.factor(0)) + self.visit(ctx.factor(1))
        else:
            return self.visit(ctx.factor())
# 1 and 2 or 3 an True
    # factor: operand (ANDOR operand)*; 
    def visitFactor(self,ctx:MPParser.FactorContext):
        operands = [self.visit(x) for x in ctx.operand] # [Intlit(1), Intlit(2),...]
        ops = [x.getText() for x in ctx.ANDOR] # ["and","or",...]
        res = operands[0]
        for i in range(0, len(ops)):
            res = BinOp(ops[1], res, operands[i+1])
        # operandlist = ctx.operand() # list [1, 2, 3, True]
        # andorlist = ctx.ANDOR()
        # return [Binary(andorlist(0).getText(), oper) for oper in operandlist]
    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):
        if(ctx.ID()):
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        else:
            return self.visit(ctx.exp())