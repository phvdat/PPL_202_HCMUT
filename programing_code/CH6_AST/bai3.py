class ASTGeneration(MPVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))


    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())


    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if(ctx.getChildCount()==0):
            return []
        else:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())


    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        typ = self.visit(ctx.mptype())
        idslist = self.visit(ctx.ids())

        # cach 1 : dung for
        # res = []  
        # for id in idlist:
        #     res += [VarDecl(id, type)]
        # return res

        # cach 2:
        return [VarDecl(iden, typ) for iden in idslist]



    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        if (ctx.INTTYPE()):
            return IntType()
        else:
            return FloatType()


    # ids: ID ',' ids | ID;
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 3:
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
        else:
            return [Id(ctx.ID().getText())]