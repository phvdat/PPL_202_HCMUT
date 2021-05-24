class ASTGeneration(MPVisitor):
    #program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.exp()))
    
    #exp: term ASSIGN exp | term;
    def visitExp(self,ctx:MPParser.ExpContext):
        if (ctx.getChildCount()==3):
            return Binary(ctx.ASSIGN().getText(),self.visit(ctx.term()),self.visit(ctx.exp()))
        else:
            return self.visit(ctx.term())
    #term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext):
        if (ctx.getChildCount()==3):
            return Binary(ctx.COMPARE().getText(),self.visit(ctx.factor(0)),self.visit(ctx.factor(1)))
        else:
            return self.visit(ctx.factor(0))
            
    #factor: factor ANDOR operand | operand; 
    def visitFactor(self,ctx:MPParser.FactorContext):
        if (ctx.getChildCount()==3):
            return Binary(ctx.ANDOR().getText(),self.visit(ctx.factor()),self.visit(ctx.operand()))
        else:
            return self.visit(ctx.operand())
            
    #operand: ID | INTLIT | BOOLIT | '(' exp ')'; 
    def visitOperand(self,ctx:MPParser.OperandContext):
        if (ctx.getChildCount()==3):
            return self.visit(ctx.exp())
        else:
            if(ctx.INTLIT()):
                return IntLiteral(ctx.INTLIT().getText())
            elif(ctx.BOOLIT()):
                return BooleanLiteral(ctx.BOOLIT().getText())
            else:
                return Id(ctx.ID().getText())
        





