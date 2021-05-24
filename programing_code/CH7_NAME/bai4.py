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
    # class Program: #decl:List[Decl]
    def visitProgram(self,ctx:Program,o:object):
        o=[[]]
        for decl in ctx.decl:
            o[0]+= [self.visit(decl,o)]
            
    # class VarDecl(Decl): #name:str,typ:Type 
    def visitVarDecl(self,ctx:VarDecl,o:object):
        n = ctx.name
        if n in o[0]: # nếu n có nằm trong o
            raise RedeclaredVariable(n)
        return n

    # class ConstDecl(Decl): #name:str,val:Lit
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        n = ctx.name
        if n in o[0]: # nếu n có nằm trong o
            raise RedeclaredConstant(n)
        return n

    # class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        n = ctx.name
        if n in o[0]: # nếu n có nằm trong o
            raise RedeclaredFunction(n)
        o[0]+= [n]
        env = [[]] + o # tạo môi trường mới
        for param in ctx.param:
            env[0]+= [self.visit(param,env)]
        for body1 in ctx.body[0]:
            env[0]+= [self.visit(body1,env)]
        for body2 in ctx.body[1]:
            self.visit(body2,env)
        return n
    
    # class IntType(Type)
    def visitIntType(self,ctx:IntType,o:object):pass


    # class FloatType(Type)
    def visitFloatType(self,ctx:FloatType,o:object):pass

    # class IntLit(Lit): #val:int
    def visitIntLit(self,ctx:IntLit,o:object):pass

    # class Id(Expr): #name:str
    def visitId(self,ctx:Id,o:object):
        n = ctx.name
        b= False
        for i in o:
            if n in i: # nếu n có nằm trong o
                b = True
                break
        if not b:
            raise UndeclaredIdentifier(n)
