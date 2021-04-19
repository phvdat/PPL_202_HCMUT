from functools import *
# program: vardecl+ EOF;

# vardecl: mptype ids ';' ;

# mptype: INTTYPE | FLOATTYPE;

# ids: ID (',' ID)*; 

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;

# and AST classes as follows:

class Program:#decl:list(VarDecl)
    pass

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class VarDecl: #variable:Id; varType: Type
    pass
class Id: #name:str
    pass
# Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?
# CACH 1
class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        vardecls = ctx.vardecl() # list vardecl
        res = []
        for vardecl in vardecls:
            res += self.visit(vardecl)
        return Program(res)
       
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return self.visit(ctx.mptype())

    def visitMptype(self,ctx:MPParser.MptypeContext):
        if (ctx.INTTYPE()):
            return IntType()
        else:
            return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        ids = ctx.ID() # lisst cac id thuoc kieu MPParser.ID() - > Id()
        res = []
        for id in ids:
            res += [Id(id.getText())]
        return res
        # return [Id(id.getText()) for id in ids] # cach2

# CÁCH 2
from functools import reduce
class ASTGeneration(MPVisitor):
    
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(reduce(lambda acc,ele: acc + self.visit(ele), ctx.vardecl(), []))

       
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return list(map(lambda x:VarDecl(x,self.visit(ctx.mptype())), self.visit(ctx.ids())))

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(id.getText()) for id in ctx.ID()] # cach2


