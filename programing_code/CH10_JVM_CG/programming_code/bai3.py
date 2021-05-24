def visitBinExpr(self, ast, o):
    e1c, e1t = self.visit(ast.e1, o)
    e2c, e2t = self.visit(ast.e2, o)
    if ast.op in ['+', '-']:
        op = self.emit.emitADDOP(ast.op,IntType(), o.frame)
        rt = IntType()
    
    if ast.op in ['*', '/']:
        op = self.emit.emitMULOP(ast.op,IntType(), o.frame)
        rt = IntType()
    
    if ast.op in ['+.']:
        op = self.emit.emitADDOP('+',FloatType(), o.frame)
        rt = FloatType()
    if ast.op in ['-.']:
        op = self.emit.emitADDOP('-',FloatType(), o.frame)
        rt = FloatType()
    
    if ast.op in ['*.']:
        op = self.emit.emitMULOP('*',FloatType(), o.frame)
        rt = FloatType()
    if ast.op in ['/.']:
        op = self.emit.emitMULOP('/',FloatType(), o.frame)
        rt = FloatType()
        
    return e1c+e2c+op, rt