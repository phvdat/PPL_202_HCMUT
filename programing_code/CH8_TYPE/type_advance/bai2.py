class Program: #decl:List[VarDecl],stmts:List[Stmt]
    pass
class VarDecl: #name:str
    pass
class Stmt(ABC): #abstract class
    pass
class Block(Stmt): #decl:List[VarDecl],stmts:List[Stmt]
    pass
class Assign(Stmt): #lhs:Id,rhs:Exp
    pass
class Exp(ABC): #abstract class
    pass
class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    pass
class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor
    pass
class IntLit(Exp): #val:int
    pass
class FloatLit(Exp): #val:float
    pass
class BoolLit(Exp): #val:bool
    pass
class Id(Exp): #name:str
    pass


def setType(id, o, typ):
    for i in o:
        if id.name == i[0]:
            i[1]= typ

class StaticCheck(Visitor):

    #decl:List[VarDecl],stmts:List[Stmt]
    def visitProgram(self, ctx: Program, o):
        o=[]
        for elem in ctx.decl:
            o += [self.visit(elem,o)]
        for elem in ctx.stmts: # ctx.stmts trả về một mảng các statement
            self.visit(elem, o)
    
    #name:str
    def visitVarDecl(self, ctx: VarDecl, o):
        for i in o:
            if i[0] == ctx.name:
                raise Redeclared(ctx)
        return [ctx.name, 'none']


    #decl:List[VarDecl],stmts:List[Stmt]
    def visitBlock(self,ctx:Block,o):
        env = []
        for decl in ctx.decl:
            env +=[self.visit(decl,env)]

        temp = [i[0] for i in env] # mảng các tên biến trong env
        for j in o:
            if j[0] in temp: # nếu có khai báo trùng => bỏ qua
                pass
            else:  
                env.append(j) # lấy all trong o(k trùng) thêm vào env
        for stmt in ctx.stmts:
            self.visit(stmt, env)

        temp=[i.name for i in ctx.decl]    # mảng các tên biến trong block
        for x in o:
            if x[0] not in temp:# tim biến  thuộc o k dc khai báo trong block
                for y in env:
                    if x[0]==y[0]:# mà dc sử dụng trong block
                        o.remove(x)
                        o.append(y)


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

    def visitId(self, ctx, o):
        for i in o:
            if ctx.name == i[0]:
                return i[1]
        raise UndeclaredIdentifier(ctx.name)
