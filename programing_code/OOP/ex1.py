class Exp(): pass
class IntLit(Exp):
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value
class FloatLit(Exp):
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value
class BinExp(Exp):
    def __init__(self, op1, op, op2):
        self.op1 = op1
        self.op = op
        self.op2 = op2
    def eval(self):
        value1 = self.op1.eval() #vi k biet tham so la gi , intlit
        value2 = self.op2.eval()
        if self.op=='+':
            return value1 + value2
        elif self.op=='-':
            return value1 - value2
        elif self.op=='*':
            return value1 * value2
        elif self.op=='/':
            return value1 / value2

class UnExp(Exp):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
    def eval(self):
        value = self.op2.eval()

        if self.op1=='-':
            return -value
        elif self.op1=='+':
            return value

x1 = IntLit(5)
print(x1.eval())