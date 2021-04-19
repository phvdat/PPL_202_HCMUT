# program: vardecls EOF;

# vardecls: vardecl vardecltail;

# vardecltail: vardecl vardecltail | ;

# vardecl: mptype ids ';' ;

# mptype: INTTYPE | FLOATTYPE;

# ids: ID ',' ids | ID;

# INTTYPE: 'int';

# FLOATTYPE: 'float';

# ID: [a-z]+ ;

# Please copy the following class into your answer and modify the bodies of its methods to count the terminal nodes in the parse tree?

class ASTGeneration(MPVisitor):
    # program: vardecls EOF;
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return 1 + self.visit(ctx.vardecls())
    # vardecls: vardecl vardecltail;

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        else:
            return 1 # thắc mắc

    # vardecl: mptype ids ';' ;
    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self, ctx: MPParser.MptypeContext):

        return 1

    # ids: ID ',' ids | ID;
    def visitIds(self, ctx: MPParser.IdsContext):
        if ctx.getChildCount() == 3:
            return 2 + self.visit(ctx.ids())
        else:
            return 1

#  bai 2
class ASTGeneration(MPVisitor):
    #     program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):

        return 1 + self.visit(ctx.vardecls())


    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):

        return 1+ self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())


    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if(ctx.getChildCount()==2):
            return 1+ self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        else:
            return 1


    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())



    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):

        return 1


    # ids: ID ',' ids | ID; 
    def visitIds(self,ctx:MPParser.IdsContext):
        if(ctx.getChildCount()==3):
            return 1+ self.visit(ctx.ids())
        else:
            return 1

# bai 3
class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)


class Program(AST):
    #decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl
    
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class VarDecl(Decl):
    #variable:Id
    #varType: Type
    def __init__(self, variable, varType):
        self.variable = variable
        self.varType = varType

    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)


class Id(AST):
    #name:string
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)


# "int a;"Program([VarDecl(Id(a),IntType)])
class ASTGeneration(MPVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))


    # vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())


    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.getChildCount() ==2 :
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        else:
            return []

    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext):
        typ = self.visit(ctx.mptype())
        idslist = self.visit(ctx.ids()) # tra ve 1 list
        return [VarDecl(x, typ) for x in idslist]


    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()


    # ids: ID ',' ids | ID;
    def visitIds(self,ctx:MPParser.IdsContext):
        if ctx.getChildCount() == 3:
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
        else:
            return [Id(ctx.ID().getText())]


# bai 5

        # "int a;" => Program([VarDecl(Id(a),IntType)])

class ASTGeneration(MPVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecl()))


    # vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext):
        # typ = self.visit(ctx.mptype())
        # idslist = self.visit(ctx.ids())
        # return [VarDecl(x, typ) for x in idslist]
        return list(map(lambda x:VarDecl(x,self.visit(ctx.mptype())), self.visit(ctx.ids())))

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        # if ctx.INTTYPE:
        #     return IntType()
        # else:
        #     return FloatType()
        return IntType() if ctx.INTTYPE else FloatType()

    # ids: ID (',' ID)*; 
    def visitIds(self,ctx:MPParser.IdsContext):
        # idslist = ctx.ID()
        # res = []
        # for i in idslist:
        #     res += Id(i.getText(i))
        # return res
        return [Id(i.getText()) for i in ctx.ID()]