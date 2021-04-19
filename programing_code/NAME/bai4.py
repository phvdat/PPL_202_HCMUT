# class Program: #decl:List[Decl]

# class Decl(ABC): #abstract class

# class VarDecl(Decl): #name:str,typ:Type

# class ConstDecl(Decl): #name:str,val:Lit

# class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])

# class Type(ABC): #abstract class

# class IntType(Type)

# class FloatType(Type)

# class Expr(ABC): #abstract class

# class Lit(Expr): #abstract class

# class IntLit(Lit): #val:int

# class Id(Expr): #name:str


class RedeclaredVariable(Exception): #name:str
    pass
class RedeclaredConstant(Exception): #name:str
    pass
class RedeclaredFunction(Exception): #name:str
    pass
class UndeclaredIdentifier(Exception): #name:str    
    pass


class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o:object):
        o=[[]]
        for decl in ctx.decl:
            o[0]+= [self.visit(decl,o)]
    def visitVarDecl(self,ctx:VarDecl,o:object):
        n = ctx.name
        if n in o[0]: # nếu n có nằm trong o
            raise RedeclaredVariable(n)
        return n
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        n = ctx.name
        if n in o[0]: # nếu n có nằm trong o
            raise RedeclaredConstant(n)
        return n
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        n = ctx.name
        if n in o[0]: # nếu n có nằm trong o
            raise RedeclaredFunction(n)
        n = ctx.name
        if n in o[0]: # nếu n có nằm trong o
            raise RedeclaredFunction(n)
        env = [[]] + o # tạo môi trường mới
        for param in ctx.param:
            env[0]+= [self.visit(param,env)]
        for body in ctx.body[0]:
            env[0]+= [self.visit(body,env)]
        for body in ctx.body[1]:
            env[0]+= [self.visit(body,env)]
        return n

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        n = ctx.name
        for i in o:
            if  n not in i: # nếu n có nằm trong o
                raise UndeclaredIdentifier(n)