# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#declarations.
    def visitDeclarations(self, ctx:BKITParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_arr.
    def visitVar_arr(self, ctx:BKITParser.Var_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardecl.
    def visitVardecl(self, ctx:BKITParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ids_list.
    def visitIds_list(self, ctx:BKITParser.Ids_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdecl.
    def visitFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameterlist.
    def visitParameterlist(self, ctx:BKITParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter.
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stm.
    def visitCall_stm(self, ctx:BKITParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stm.
    def visitReturn_stm(self, ctx:BKITParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment_stm.
    def visitAssignment_stm(self, ctx:BKITParser.Assignment_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression1.
    def visitExpression1(self, ctx:BKITParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression2.
    def visitExpression2(self, ctx:BKITParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression3.
    def visitExpression3(self, ctx:BKITParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expressionlist.
    def visitExpressionlist(self, ctx:BKITParser.ExpressionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operands.
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        return self.visitChildren(ctx)



del BKITParser