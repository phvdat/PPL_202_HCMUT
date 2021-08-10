def setType(id, o, typ):
    for x in o:
        if id.name == x[0]:
            x[1] = typ
            return
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o=[]
        for decl in ctx.decl:
            o+=[self.visit(decl, o)]
        for stmt in ctx.stmts:
            self.visit(stmt, o)

    def visitVarDecl(self,ctx:VarDecl,o):
        n = ctx.name
        for x in o:
            if n == x[0]:
                raise Redeclared(ctx)
        return [n, 'none']

    def visitBlock(self,ctx:Block,o):
        env = []
        for decl in ctx.decl:
            env+=[self.visit(decl, env)]
        for stmt in ctx.stmts:
            self.visit(stmt, env+o)
        

    #lhs:Id,rhs:Exp
    def visitAssign(self, ctx: Assign, o):
        typ1 = self.visit(ctx.lhs, o)
        typ2 = self.visit(ctx.rhs, o)
        if typ1 =='none' and typ2 == 'none':
            raise TypeCannotBeInferred(ctx)
        if typ1 == 'none':
            setType(ctx.lhs, o, typ2)
            typ1 = typ2
        if typ2== 'none':
            setType(ctx.rhs, o, typ1)
            typ2 = typ1
        if typ1!=typ2:
            raise TypeMismatchInStatement(ctx)

    #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self, ctx: BinOp, o):
        typ1 = self.visit(ctx.e1, o)
        typ2 = self.visit(ctx.e2, o)
        if(ctx.op in ['+', '-', '*', '/']):
            if typ1 == 'none':
                setType(ctx.e1,o,'int')
                typ1 ='int'
            if typ2 =='none':
                setType(ctx.e2,o,'int')
                typ2 ='int'
            if typ1 != 'int' or typ2 != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'int'

        if(ctx.op in ['+.', '-.', '*.', '/.']):
            if typ1 =='none':
                setType(ctx.e1,o,'float')
                typ1 = 'float'
            if typ2 =='none':
                setType(ctx.e2,o,'float')
                typ2 ='float'
            if typ1 != 'float' or typ2 != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        if ctx.op in ['=', '>']:
            if typ1 =='none':
                setType(ctx.e1,o,'int')
                typ1 ='int'
            if typ2 =='none':
                setType(ctx.e2,o,'int')
                typ2 ='int'
            if typ1 != 'int' or typ2 != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        if ctx.op in ['=.', '>.']:
            if typ1 =='none':
                setType(ctx.e1,o,'float')
                typ1 ='float'
            if typ2 =='none':
                setType(ctx.e2,o,'float')
                typ2 ='float'
            if typ1 != 'float' or typ2 != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        if ctx.op in ['!', '&&', '||', '>b', '=b']:
            if typ1 =='none':
                setType(ctx.e1,o,'bool')
                typ1 ='bool'
            if typ2 =='none':
                setType(ctx.e2,o,'bool')
                typ2 ='bool'
            if typ1 != 'bool' or typ2 != 'bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'

    def visitUnOp(self, ctx: UnOp, o):
        typ = self.visit(ctx.e, o)
        if ctx.op == '-':
            if typ == 'none':
                setType(ctx.e, o, 'int')
                typ ='int'
            if typ != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'int'
        if ctx.op == '-.':
            if typ =='none':
                setType(ctx.e, o, 'float')
                typ ='float'
            if typ != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        if ctx.op == '!':
            if typ =='none':
                setType(ctx.e, o, 'bool')
                typ ='bool'
            if typ != 'bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        if ctx.op == 'i2f':
            if typ =='none':
                setType(ctx.e, o, 'int')
                typ ='int'
            if typ != 'int':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        if ctx.op == 'floor':
            if typ =='none':
                setType(ctx.e, o, 'float')
                typ ='float'
            if typ != 'float':
                raise TypeMismatchInExpression(ctx)
            return 'int'

    def visitIntLit(self, ctx: IntLit, o):
        return 'int'

    def visitFloatLit(self, ctx, o):
        return 'float'

    def visitBoolLit(self, ctx, o):
        return 'bool'

    def visitId(self,ctx,o):
        for x in o:
            if ctx.name == x[0]:
                return x[1]
        raise UndeclaredIdentifier(ctx.name)