def setType(name, o, typ):
    for x in o:
        if name == x[0]:
            x[1] = typ
            return
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o= []
        for decl in ctx.decl:
            o+= [self.visit(decl, o)]
        for stmt in ctx.stmts:
            self.visit(stmt, o)

    def visitVarDecl(self,ctx:VarDecl,o):
        n = ctx.name
        for x in o:
            if n == x[0]:
                raise Redeclared(ctx)
        return [n, 0]

    def visitFuncDecl(self,ctx:FuncDecl,o):
        n = ctx.name
        for x in o:
            if n==x[0]:
                raise Redeclared(ctx)
        env = []
        for param in ctx.param:
            env+= [self.visit(param, env)]
        
        for local in ctx.local:
            env+= [self.visit(local, env)]
        for stmt in ctx.stmts:
            self.visit(stmt, env + o)
        paramlst = []
        for x in env:
            if x[0] in [param.name for param in ctx.param]:
                paramlst +=[x]
        return [n, 4] + [paramlst]
    def visitCallStmt(self,ctx:CallStmt,o):
        n =  ctx.name
        lst1 = [self.visit(elem, o) for elem in ctx.args]
        finded = False
        for x in o:
            if n == x[0] and 4 == x[1]:
                finded = True
                for arg in ctx.args:
                    lst2 = x[2]
                    if len(lst2) != len(lst1):
                        raise TypeMismatchInStatement(ctx)
                    count = 0
                    for i, j in zip(lst1, lst2):
                        if i == 0 and j[1] == 0:
                            raise TypeCannotBeInferred(ctx)
                        elif j[1] == 0:
                            j[1] = i
                            setType(j[0], o, i)
                        elif i == 0:
                            i = j
                            setType(ctx.args[count].name, o, j)
                        elif i != j[1]:
                            raise TypeMismatchInStatement(ctx)
                        count+=1
                break
        if not finded:
            raise UndeclaredIdentifier(ctx.name)

    def visitAssign(self,ctx:Assign,o):
    
        left= self.visit(ctx.lhs, o)
        right = self.visit(ctx.rhs, o)
        if right == 0 and left == 0:
            raise TypeCannotBeInferred(ctx)
        elif right == 0:
            setType(ctx.rhs.name, o, left)
            right = left
        elif left == 0:
            setType(ctx.lhs.name, o, right)
            left = right
        elif right != left:
            raise TypeMismatchInStatement(ctx)
            
    def visitIntLit(self,ctx:IntLit,o):
        return 1

    def visitFloatLit(self,ctx,o):
        return 2

    def visitBoolLit(self,ctx,o):
        return 3
    def visitId(self,ctx,o):
        for x in o:
            if ctx.name == x[0]:
                return x[1]
        raise UndeclaredIdentifier(ctx.name)