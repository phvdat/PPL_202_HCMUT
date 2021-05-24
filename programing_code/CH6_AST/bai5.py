from functools import *
# vd:
# "int a;"
# Program([VarDecl(Id(a),IntType)])
# CACH 1
class ASTGeneration(MPVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        vardecls = ctx.vardecl() # list vardecl
        res = []
        for vardecl in vardecls:
            res += self.visit(vardecl)
        return Program(res)


    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return list(map(lambda x : VarDecl(x, self.visit(ctx.mptype())), self.visit(ctx.ids())))


    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        if (ctx.INTTYPE()):
            return IntType()
        else:
            return FloatType()


    # ids: ID (',' ID)*; 
    def visitIds(self,ctx:MPParser.IdsContext):
        ids = ctx.ID() # list cac id thuoc kieu MPParser.ID() - > Id()
        res = []
        for id in ids:
            res += [Id(id.getText())]
        return res

# CACH 2
from functools import reduce
class ASTGeneration(MPVisitor):
    
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(reduce(lambda acc,ele: acc + self.visit(ele), ctx.vardecl(), []))

       
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return list(map(lambda x:VarDecl(x,self.visit(ctx.mptype())), self.visit(ctx.ids())))

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(id.getText()) for id in ctx.ID()]


