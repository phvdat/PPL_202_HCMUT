trait AST
case class Program(sl:Stmt) extends AST
trait Stmt extends AST
case class Assign(id:String,e:Exp) extends Stmt
trait Exp ixtends AST
case class BinOp(op:String,el:Exp,e2:Exp) extends Exp
case class Id(id:String) extends Exp
case class Intlit(lit:Int) extends Exp

class ASTGen extends MCBaseVisitor[AST] {
	/* term : ID 1 INT 1 LP exp RP */
	override def visitTerm(ctx:TermContext) =
		if (ctx.getChildCount() == 3) ctx.exp().accept(this)
		else if (ctx.ID != null) Id(ctx.ID.getText)
		else Intlit(ctx.INT.getText.tolnt)

	/* exp : exp ADDOP term 1 term */
	override def visitExp(ctx:ExpContext) = {
		if (ctx.getChildCount() == 1) ctx.term().accept
		else BinOp(ctx.ADDOP.getText,ctx.exp().accept(this).aslnstanceOf[Exp]
			,ctx.term.accept(this).asInstanceOf[Exp])

	/* assign : ID ASSIGN exp SEMI */
	override def visitAssign(ctx:AssignContext)
		Assign(ctx.ID.getText,ctx.exp.accept(this).asInstanceOf[Exp]

	/* stmt : assign */
	override def visitStmt(ctx:StmtContext) = ctx.getChild(0).accept(this)
	
	/* prog: stmt */
	override def visitProgram(ctx:ProgramContext) = ctx.getChild(1).accept(this)