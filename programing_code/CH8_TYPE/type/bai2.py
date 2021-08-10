class StaticCheck(Visitor):
    # decl:List[VarDecl],exp:Exp
    def visitProgram(self, ctx: Program, o):
        o = []
        for x in ctx.decl:
            o += self.visit(x, o)
        self.visit(ctx.exp, o)

    # name:str,typ:Type
    def visitVarDecl(self, ctx: VarDecl, o):
        return [ctx]

    # op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=
    def visitBinOp(self,ctx:BinOp,o):
        typ1 = self.visit(ctx.e1,o)
        typ2 = self.visit(ctx.e2,o)
        
        if ctx.op in ['+','-','*'] :
            if type(typ1)==BoolType or type(typ2)==BoolType:
                raise TypeMismatchInExpression(ctx)
            if type(typ1)!=type(typ2):
                return FloatType()
            return IntType()
        if ctx.op == '/' :
            if type(typ1) ==BoolType or type(typ2) == BoolType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if ctx.op in ['!', '&&', '||' ]:
            if type(typ1) !=BoolType or type(typ2) != BoolType:
                raise TypeMismatchInExpression(ctx)
            return typ1
        if ctx.op in ['>', '<', '==','!=']:
            if type(typ1) != type(typ2):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    # op:str,e:Exp #op is -, !
    def visitUnOp(self,ctx:UnOp,o):
        typ = self.visit(ctx.e,o)
        if ctx.op == '-':
            if type(typ) == BoolType:
                raise TypeMismatchInExpression(ctx)
            return typ
        if ctx.op =='!':
            if type(typ) == IntType or type(typ) == FloatType:
                raise TypeMismatchInExpression(ctx)
            return typ
        

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()

    # name:str
    def visitId(self, ctx, o):
        for decl in o:
            if decl.name == ctx.name:
                return decl.typ
        raise UndeclaredIdentifier(ctx.name)