# program: exp EOF;

# exp: term ASSIGN exp | term;

# term: factor COMPARE factor | factor;

# factor: factor ANDOR operand | operand; 

# operand: ID | INTLIT | BOOLIT | '(' exp ')';

# INTLIT: [0-9]+ ;

# BOOLIT: 'True' | 'False' ;

# ANDOR: 'and' | 'or' ;

# ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

# COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

# ID: [a-z]+ ;

# and AST classes as follows:

class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Expr(AST):
    __metaclass__ = ABCMeta
    pass

class Binary(Expr):
    #op:string: 
    #left:Expr
    #right:Expr
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return "Binary(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)

class Id(Expr):
    #value:string
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Id(" + self.value + ")"

    def accept(self, v, param):
        return v.visitId(self, param)

class IntLiteral(Expr):
    #value:int
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

class BooleanLiteral(Expr):
    #value:boolean
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BooleanLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)


# Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

class ASTGeneration(MPVisitor):
    #program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return p(self.visit(ctx.exp()))
    
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
            else:
                if(ctx.BOOLIT()):
                    return BooleanLiteral(ctx.BOOLIT().getText())
                else:
                    return Id(ctx.ID().getText())
        





