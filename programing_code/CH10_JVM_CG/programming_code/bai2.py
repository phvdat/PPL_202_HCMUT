def visitFloatLiteral(self, ast, o):
    return self.emit.emitPUSHFCONST(ast.value, o.frame), FloatType()