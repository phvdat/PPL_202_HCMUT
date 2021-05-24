# class Program: #decl:List[Decl]

# class Decl(ABC): #abstract class

# class VarDecl(Decl): #name:str,typ:Type

# class ConstDecl(Decl): #name:str,val:Lit

# class Type(ABC): #abstract class

# class IntType(Type)

# class FloatType(Type)

# class Lit(ABC): #abstract class

# class IntLit(Lit): #val:int


class RedeclaredDeclaration(Exception): #name:str
    pass


class StaticCheck(Visitor):
    # class Program: #decl:List[Decl]
    def visitProgram(self,ctx:Program,o:object):
        o=[]
        for decl in ctx.decl:
            o+= [self.visit(decl,o)]


    # class VarDecl(Decl): #name:str,typ:Type
    def visitVarDecl(self,ctx:VarDecl,o:object):
        n = ctx.name
        if n in o: # nếu n có nằm trong o
            raise RedeclaredDeclaration(n)
        return n

    # class ConstDecl(Decl): #name:str,val:Lit
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        n = ctx.name
        if n in o:
            raise RedeclaredDeclaration(n)
        return n
    
    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass