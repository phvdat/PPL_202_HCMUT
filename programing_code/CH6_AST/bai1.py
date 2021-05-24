class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):

        return self.visit(ctx.vardecls()) +1

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if ctx.getChildCount() == 0:
            return 0
        else:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return self.visit(ctx.mptype()) +self.visit(ctx.ids()) +1

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return 1

    def visitIds(self, ctx: MPParser.IdsContext):
        if(ctx.getChildCount() == 3):
            return 2 + self.visit(ctx.ids())
        else:
            return 1