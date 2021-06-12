def visitId(self, ast, o):
    sym = next(filter(lambda y: y.name== ast.name, o.sym), False)
    if type(sym.value) is Index:
        code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
    else:
        code = self.emit.emitGETSTATIC(sym.value.value +'.'+ sym.name, sym.mtype, o.frame)
    typ = sym.mtype
    return code, typ