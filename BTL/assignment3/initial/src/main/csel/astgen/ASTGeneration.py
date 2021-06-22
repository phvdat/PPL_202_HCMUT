# Pham Van Dat
# 1811892

from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from AST import *
from functools import reduce


class ASTGeneration(CSELVisitor):
    # program:#declaration:List[Declare]
    def visitProgram(self, ctx: CSELParser.ProgramContext):
        declList = []
        for x in ctx.declaration():
            decl = self.visitDeclaration(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return Program(declList)

    #*********************************************************
    #*********************VAR_DECLARATION**********************
    #*********************************************************
    
    def visitDeclaration(self, ctx: CSELParser.DeclarationContext):
        return self.visit(ctx.getChild(0))
    
    # var_declare:	LET vars_list SEMI;
    def visitVar_declare(self, ctx: CSELParser.Var_declareContext):
        return self.visit(ctx.vars_list())

    # vars_list: var_typ_asg COMMA vars_list | var_typ_asg;
    def visitVars_list(self, ctx: CSELParser.Vars_listContext):
        if ctx.vars_list():
            return [self.visit(ctx.var_typ_asg())] + self.visit(ctx.vars_list())
        else:
            return [self.visit(ctx.var_typ_asg())]

    # var_typ_asg:	ID array_ref?  (COLON data_types)? (ASSIGN exp)? ;
    def visitVar_typ_asg(self, ctx: CSELParser.Var_typ_asgContext):
        
        if ctx.array_ref():
            array_ref_temp = self.visit(ctx.array_ref())
        else:
            array_ref_temp = None

        if ctx.data_types():
            data_types_temp = self.visit(ctx.data_types())
        else:
            data_types_temp = NoneType()

        if ctx.exp():
            exp_temp = self.visit(ctx.exp())
        else:
            exp_temp = None

        return VarDecl(Id(ctx.ID().getText()), array_ref_temp, data_types_temp, exp_temp)

    #*********************************************************
    #***********************CONSTANT************************
    #*********************************************************

    def visitConstant_declare(self, ctx: CSELParser.Constant_declareContext):
        return self.visit(ctx.constant_id_list())
    
    def visitConstant_id_list(self, ctx: CSELParser.Constant_id_listContext):
        return [self.visit(x) for x in ctx.constant_assign()] if ctx.constant_assign() else []

    def visitConstant_assign(self, ctx: CSELParser.Constant_assignContext):
        if ctx.array_ref():
            array_ref_temp = self.visit(ctx.array_ref())
        else:
            array_ref_temp = None
        if ctx.data_types():
            data_types_temp = self.visit(ctx.data_types())
        else:
            data_types_temp = NoneType()

        return ConstDecl(Id(ctx.ID_WITH_DOLLAR().getText()), array_ref_temp, data_types_temp, self.visit(ctx.exp()))


    #*********************************************************
    #***********************ARRAY****************************
    #*********************************************************

    def visitArray_ref(self, ctx: CSELParser.Array_refContext):
        if ctx.index_op():
            return self.visit(ctx.index_op())
        else:
            return []
    
    # def visitDimen_list(self, ctx: CSELParser.Dimen_listContext):
    #     if ctx.index_op():
    #         return [self.visit(ctx.exp())]  + self.visit(ctx.index_op())
    #     else:
    #         return [self.visit(ctx.exp())]

    def visitData_types(self, ctx: CSELParser.Data_typesContext):
        if ctx.NUMBER():
            return NumberType()
        if ctx.STRING():
            return StringType()
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.JSON():
            return JSONType()


    #*********************************************************
    #***********************FUNCTION**************************
    #*********************************************************

    # func_declare: FUNCTION ID LP params_list? RP  LCB statementsList? RCB;
    def visitFunc_declare(self, ctx: CSELParser.Func_declareContext):
        paraList = self.visit(ctx.params_list()) if ctx.params_list() else []
        block = self.visit(ctx.statementsList()) if ctx.statementsList() else []
        return FuncDecl(Id(ctx.ID().getText()),paraList,block)

    # params_list:		param (COMMA param)* ;
    def visitParams_list(self, ctx: CSELParser.Params_listContext):
        return [self.visit(x) for x in ctx.param()] if ctx.param() else []
            

    def visitParam(self, ctx: CSELParser.ParamContext):
        if ctx.array_ref():
            array_ref_temp = self.visit(ctx.array_ref())
        else:
            array_ref_temp = None

        if ctx.ID():
            return VarDecl(Id(ctx.ID().getText()), array_ref_temp, NoneType(), None )
        elif ctx.ID_WITH_DOLLAR():
            return VarDecl(Id(ctx.ID_WITH_DOLLAR().getText()), array_ref_temp, NoneType(), None )
    #*********************************************************
    #***********************STATEMENT*************************
    #*********************************************************

    def visitStmt(self, ctx: CSELParser.StmtContext):
        if ctx.var_declare():
            return self.visit(ctx.var_declare())
        elif ctx.constant_declare():
            return self.visit(ctx.constant_declare())
        else:
            return [self.visit(ctx.getChild(0))]
    #asign
    def visitAssign_stmt(self, ctx: CSELParser.Assign_stmtContext):
        if ctx.exp7():
            return Assign(self.visit(ctx.exp7()), self.visit(ctx.exp()))
        elif ctx.ID():
            return Assign(Id(ctx.ID().getText()), self.visit(ctx.exp()))
        
    #if
    def visitIf_stmt(self, ctx: CSELParser.If_stmtContext):
        if ctx.else_func():
            if ctx.elseif_list():
                return If([(self.visit(ctx.exp()), self.visit(ctx.statementsList()))] + self.visit(ctx.elseif_list()),self.visit(ctx.else_func()) )
            else:
                return If([(self.visit(ctx.exp()), self.visit(ctx.statementsList()))], self.visit(ctx.else_func()))
        else:
            if ctx.elseif_list():
                return If([(self.visit(ctx.exp()), self.visit(ctx.statementsList()))] + self.visit(ctx.elseif_list()),[])
            else:
                return If([(self.visit(ctx.exp()), self.visit(ctx.statementsList()))] ,[])
        

    
    def visitElseif_list(self, ctx: CSELParser.Elseif_listContext):
        return [self.visit(x) for x in ctx.elseif_func()] if ctx.elseif_func() else []
    
    def visitElseif_func(self, ctx: CSELParser.Elseif_funcContext):
        return (self.visit(ctx.exp()), self.visit(ctx.statementsList()))
    
    def visitElse_func(self, ctx: CSELParser.Else_funcContext):
        if ctx.statementsList():
            return self.visit(ctx.statementsList())
        else:
            return []
    #vonglap
    def visitWhile_stmt(self, ctx: CSELParser.While_stmtContext):
        if ctx.statementsList():
            return While(self.visit(ctx.exp()), self.visit(ctx.statementsList()))
        else:
            return While(self.visit(ctx.exp()), [])
    
    def visitFor_stmt(self, ctx: CSELParser.For_stmtContext):
        return self.visitChildren(ctx)
    
    def visitFor_in_stmt(self, ctx: CSELParser.For_in_stmtContext):
        if ctx.statementsList():
            return ForIn(Id(ctx.ID().getText()), self.visit(ctx.exp()), self.visit(ctx.statementsList()))
        else:
            return ForIn(Id(ctx.ID().getText()), self.visit(ctx.exp()), [])
    
    def visitFor_of_stmt(self, ctx: CSELParser.For_of_stmtContext):
        if ctx.statementsList():
            return ForOf(Id(ctx.ID().getText()), self.visit(ctx.exp()), self.visit(ctx.statementsList()))
        else:
            return ForOf(Id(ctx.ID().getText()), self.visit(ctx.exp()), [])
    # break, continue, return
    def visitBrk_stmt(self, ctx: CSELParser.Brk_stmtContext):
        return Break()
    
    def visitCont_stmt(self, ctx: CSELParser.Cont_stmtContext):
        return Continue()
    
    def visitRet_stmt(self, ctx: CSELParser.Ret_stmtContext):
        return self.visitChildren(ctx)

    def visitRet_stmt_proc(self, ctx: CSELParser.Ret_stmt_procContext):
        return Return(None)
    
    def visitRet_stmt_func(self, ctx: CSELParser.Ret_stmt_funcContext):
        return Return(self.visit(ctx.exp()))
    #Call
    def visitCall_stmt(self, ctx: CSELParser.Call_stmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.exps_list())) if ctx.exps_list() else CallStmt(Id(ctx.ID().getText()), [])
    
    def visitStatementsList(self, ctx: CSELParser.StatementsListContext):
        if ctx.statementsList():
            return self.visit(ctx.stmt()) + self.visit(ctx.statementsList())
        elif ctx.stmt():
            return self.visit(ctx.stmt())
        else:
            return []
 

    #*********************************************************
    #********************* EXPRESSIONS ***********************
    #*********************************************************

    def visitExp(self, ctx: CSELParser.ExpContext):
            if ctx.ADDS():
                return BinaryOp(ctx.ADDS().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            elif ctx.EQS() :
                return BinaryOp(ctx.EQS().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
            else:
                return self.visit(ctx.exp1(0))

    
    def visitExp1(self, ctx: CSELParser.Exp1Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp2(0))
        else:
            return BinaryOp(self.visit(ctx.relation()),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))

    def visitExp2(self, ctx: CSELParser.Exp2Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp3())
        else:
            if ctx.AND():
                return BinaryOp(ctx.AND().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
            else:
                return BinaryOp(ctx.OR().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))

    def visitExp3(self, ctx: CSELParser.Exp3Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())

    def visitExp4(self, ctx: CSELParser.Exp4Context):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self, ctx: CSELParser.Exp5Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp6())
        else:
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp5()))
            

    def visitExp6(self, ctx: CSELParser.Exp6Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp7())
        else:
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.exp6()))

    def visitExp7(self, ctx: CSELParser.Exp7Context):
        if ctx.index_op():
            return ArrayAccess(self.visit(ctx.exp7()), self.visit(ctx.index_op()))
        elif ctx.key_op():
            return JSONAccess(self.visit(ctx.exp7()), self.visit(ctx.key_op()) )
        else:
            return self.visit(ctx.exp8())
    def visitExp8(self, ctx: CSELParser.Exp8Context):
        return self.visit(ctx.getChild(0))

    def visitFuncall(self, ctx: CSELParser.FuncallContext):
        if ctx.exps_list():
            return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.exps_list()))
        else:
            return CallExpr(Id(ctx.ID().getText()), [])

    def visitOperands(self, ctx: CSELParser.OperandsContext):
        if ctx.LP():
            return self.visit(ctx.exp())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.ID_WITH_DOLLAR():
            return Id(ctx.ID_WITH_DOLLAR().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())

    def visitRelation(self, ctx: CSELParser.RelationContext):
        return ctx.getChild(0).getText()

    def visitIndex_op(self, ctx: CSELParser.Index_opContext):
        if ctx.index_op():
            return [self.visit(ctx.exp())] + self.visit(ctx.index_op())
        else:
            return [self.visit(ctx.exp())]

    def visitKey_op(self, ctx: CSELParser.Key_opContext):
        if ctx.key_op():
            return  self.visit(ctx.key_op()) + [self.visit(ctx.exp())]
        else:
            return [self.visit(ctx.exp())]



    def visitExps_list(self, ctx: CSELParser.Exps_listContext):
        return [self.visit(x) for x in ctx.exp()] if ctx.exp() else []

    # ************************************************************
    # ************************ LITERALS **************************
    # ************************************************************
    
    def visitLiteral(self, ctx: CSELParser.LiteralContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(str(ctx.NUMBER_LIT())))

        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())

        elif ctx.BOOLEAN_LIT():
            return BooleanLiteral(ctx.BOOLEAN_LIT())

        elif ctx.json_lit():
            return JSONLiteral(self.visit(ctx.json_lit()))

        elif ctx.array_lit():
            return ArrayLiteral(self.visit(ctx.array_lit()))
        
    # array_lit
    def visitArray_lit(self, ctx: CSELParser.Array_litContext):
        if ctx.array_list():
            return self.visit(ctx.array_list())
        else:
            return []
    def visitArray_list(self, ctx: CSELParser.Array_listContext):
        if ctx.array_list():
            return [self.visit(ctx.literal())] + self.visit(ctx.array_list())
        else:
            return [self.visit(ctx.literal())]

    # json_lit
    def visitJson_lit(self, ctx: CSELParser.Json_litContext):
        if ctx.json_elems_list():
            return self.visit(ctx.json_elems_list())
        else:
            return []

    def visitJson_elems_list(self, ctx: CSELParser.Json_elems_listContext):
        if ctx.json_elems_list():
            return [self.visit(ctx.json_elems())] + self.visit(ctx.json_elems_list())
        else:
            return [self.visit(ctx.json_elems())]

    def visitJson_elems(self, ctx: CSELParser.Json_elemsContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.literal()))