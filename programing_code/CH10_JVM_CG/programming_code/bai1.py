def visitIntLiteral(self, ast, o):
    return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()