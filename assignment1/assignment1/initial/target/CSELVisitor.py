# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSELParser import CSELParser
else:
    from CSELParser import CSELParser

# This class defines a complete generic visitor for a parse tree produced by CSELParser.

class CSELVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#declaration.
    def visitDeclaration(self, ctx:CSELParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_declare.
    def visitVar_declare(self, ctx:CSELParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#vars_list.
    def visitVars_list(self, ctx:CSELParser.Vars_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_typ_asg.
    def visitVar_typ_asg(self, ctx:CSELParser.Var_typ_asgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#constant_declare.
    def visitConstant_declare(self, ctx:CSELParser.Constant_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#constant_id_list.
    def visitConstant_id_list(self, ctx:CSELParser.Constant_id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#constant_assign.
    def visitConstant_assign(self, ctx:CSELParser.Constant_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#id_array.
    def visitId_array(self, ctx:CSELParser.Id_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#number_list.
    def visitNumber_list(self, ctx:CSELParser.Number_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#data_types.
    def visitData_types(self, ctx:CSELParser.Data_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#func_declare.
    def visitFunc_declare(self, ctx:CSELParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#params_list.
    def visitParams_list(self, ctx:CSELParser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#param.
    def visitParam(self, ctx:CSELParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stmt.
    def visitStmt(self, ctx:CSELParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSELParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_operator.
    def visitIndex_operator(self, ctx:CSELParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_operator.
    def visitKey_operator(self, ctx:CSELParser.Key_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#if_stmt.
    def visitIf_stmt(self, ctx:CSELParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#elseif_list.
    def visitElseif_list(self, ctx:CSELParser.Elseif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#elseif_func.
    def visitElseif_func(self, ctx:CSELParser.Elseif_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#else_func.
    def visitElse_func(self, ctx:CSELParser.Else_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#while_stmt.
    def visitWhile_stmt(self, ctx:CSELParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_stmt.
    def visitFor_stmt(self, ctx:CSELParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_in_stmt.
    def visitFor_in_stmt(self, ctx:CSELParser.For_in_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_of_stmt.
    def visitFor_of_stmt(self, ctx:CSELParser.For_of_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#brk_stmt.
    def visitBrk_stmt(self, ctx:CSELParser.Brk_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#cont_stmt.
    def visitCont_stmt(self, ctx:CSELParser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#ret_stmt.
    def visitRet_stmt(self, ctx:CSELParser.Ret_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#ret_stmt_proc.
    def visitRet_stmt_proc(self, ctx:CSELParser.Ret_stmt_procContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#ret_stmt_func.
    def visitRet_stmt_func(self, ctx:CSELParser.Ret_stmt_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#call_stmt.
    def visitCall_stmt(self, ctx:CSELParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#statementsList.
    def visitStatementsList(self, ctx:CSELParser.StatementsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp.
    def visitExp(self, ctx:CSELParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#operands.
    def visitOperands(self, ctx:CSELParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#relation.
    def visitRelation(self, ctx:CSELParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_and_key_op.
    def visitIndex_and_key_op(self, ctx:CSELParser.Index_and_key_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_op.
    def visitIndex_op(self, ctx:CSELParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_op.
    def visitKey_op(self, ctx:CSELParser.Key_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#funcall.
    def visitFuncall(self, ctx:CSELParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exps_list.
    def visitExps_list(self, ctx:CSELParser.Exps_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#literal.
    def visitLiteral(self, ctx:CSELParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_lit.
    def visitArray_lit(self, ctx:CSELParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_list.
    def visitArray_list(self, ctx:CSELParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_lit.
    def visitJson_lit(self, ctx:CSELParser.Json_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_elems_list.
    def visitJson_elems_list(self, ctx:CSELParser.Json_elems_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_elems.
    def visitJson_elems(self, ctx:CSELParser.Json_elemsContext):
        return self.visitChildren(ctx)



del CSELParser