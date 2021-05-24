    def visitBinExpr(self, ast, o):
        e1c, e1t = self.visit(ast.e1, o)
        e2c, e2t = self.visit(ast.e2, o)
        op = None
        rt = None

        if type(e1t) is type(e2t):
            rt = e1t
        elif type(e1t) is IntType() and type(e2t) is FloatType():
            e1c = e1c + self.emit.emitI2F(o.frame)
            rt = e2t
        elif type(e1t) is FloatType() and type(e2t) is IntType():
            e2c = e2c + self.emit.emitI2F(o.frame)
            rt = e1t

        if ast.op in ['+', '-']:
            op = self.emit.emitADDOP(ast.op,rt, o.frame)

        elif ast.op == '*':
            op = self.emit.emitMULOP(ast.op,rt, o.frame)
        elif ast.op == '*':
            if type(e1t) is IntType():
                e1c = e1c + self.emit.emitI2F(o.frame)
            if type(e2t) is IntType():
                e2c = e2c + self.emit.emitI2F(o.frame)
            rt = FloatType()
            op = self.emit.emitMULOP(ast.op, FloatType(), o.frame)
        elif ast.op in ['>','<','>=','<=','!=','==']:
            op = self.emit.emitREOP(ast.op, rt, o.frame)

        return e1c+e2c+op, rt