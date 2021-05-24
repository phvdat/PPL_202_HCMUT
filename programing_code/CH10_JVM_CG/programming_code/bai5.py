def visitId(self, ast, o):
    sym = list(filter(lambda  y: y.name == ast.name, o.sym))[0]