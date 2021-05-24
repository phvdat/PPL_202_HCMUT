# class Program: #decl:List[Decl]

# class Decl(ABC): #abstract class

# class VarDecl(Decl): #name:str,typ:Type

# class ConstDecl(Decl): #name:str,val:Lit

# class FuncDecl(Decl): #name:str,param:List[VarDecl],body:List[Decl]

# class Type(ABC): #abstract class

# class IntType(Type)

# class FloatType(Type)

# class Lit(ABC): #abstract class

# class IntLit(Lit): #val:int

class RedeclaredVariable(Exception): #name:str
    pass
class RedeclaredConstant(Exception): #name:str
    pass
class RedeclaredFunction(Exception): #name:str
    pass

# cach 1
# class StaticCheck(Visitor):
    
#     def visitProgram(self,ctx:Program,o:object):
#         o=[]
#         for decl in ctx.decl:
#             o+= [self.visit(decl,o)]

#     def visitVarDecl(self,ctx:VarDecl,o:object):
#         n = ctx.name
#         if n in o: # nếu n có nằm trong o
#             raise RedeclaredVariable(n)
#         return n

#     def visitConstDecl(self,ctx:ConstDecl,o:object):
#         n = ctx.name
#         if n in o: # nếu n có nằm trong o
#             raise RedeclaredConstant(n)
#         return n

#     def visitFuncDecl(self,ctx:FuncDecl,o:object):
#         n = ctx.name
#         if n in o: # nếu n có nằm trong o
#             raise RedeclaredFunction(n)
#         o=[]
#         for param in ctx.param:
#             o+= [self.visit(param,o)]
#         for body in ctx.body:
#             o+= [self.visit(body,o)]      
#         return n
#         # cách này k hiệu quả trong bài 4 : cần kiêm tra undeclaration

#     def visitIntType(self,ctx:IntType,o:object):pass

#     def visitFloatType(self,ctx:FloatType,o:object):pass

#     def visitIntLit(self,ctx:IntLit,o:object):pass


# cách của thầy
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


    # class FuncDecl(Decl): #name:str,param:List[VarDecl],body:List[Decl]
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        n = ctx.name
        if n in o[0]: # nếu n có nằm trong o
            raise RedeclaredFunction(n)
        env = [[]] + o # tạo môi trường mới
        for param in ctx.param:
            env[0]+= [self.visit(param,env)]
        for body in ctx.body:
            env[0]+= [self.visit(body,env)]      
        return n

    # class IntType(Type)
    def visitIntType(self,ctx:IntType,o:object):pass

    # class FloatType(Type)
    def visitFloatType(self,ctx:FloatType,o:object):pass

    # class IntLit(Lit): #val:int
    def visitIntLit(self,ctx:IntLit,o:object):pass