from abc import ABC
class Exp(ABC):
    def eval(self): pass
    def printPrefix(self): pass
    def printPostfix(self): pass
    def accept(self, className):
        if isinstance(className, Eval):
            return self.eval()
        if isinstance(className, PrintPrefix):
            return self.printPrefix()
        if isinstance(className, PrintPostfix):
            return self.printPostfix()


class Eval():
    pass
class PrintPrefix():
    pass
class PrintPostfix():
    pass

class IntLit(Exp):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def printPrefix(self):
        return str(self.value)

    def printPostfix(self):
        return str(self.value)


class FloatLit(Exp):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def printPrefix(self):
        return str(self.value)

    def printPostfix(self):
        return str(self.value)


class BinExp(Exp):
    def __init__(self, first, op, second):
        self.first = first
        self.op = op
        self.second = second

    def eval(self):
        value1 = self.first.eval()  # vi k biet tham so la gi , intlit
        value2 = self.second.eval()
        if self.op == '+':
            return value1 + value2
        elif self.op == '-':
            return value1 - value2
        elif self.op == '*':
            return value1 * value2
        elif self.op == '/':
            return value1 / value2

    def printPrefix(self):
        return str(self.op) + ' ' + str(self.first.printPrefix()) + ' ' + str(self.second.printPrefix()) + ' '

    def printPostfix(self):
        return str(self.first.printPostfix()) + ' ' + str(self.second.printPostfix()) + ' ' + str(self.op)


class UnExp(Exp):
    def __init__(self, op, second):
        self.op = op
        self.second = second
    def eval(self):
        value = self.second.eval()
        if self.op == '-':
            return -value
        elif self.op == '+':
            return value
    def printPrefix(self):
        return self.op+'. ' + str(self.second.eval())
    def printPostfix(self):
        return str(self.second.eval()) +' '+ self.op+'.'

x = IntLit(5)
print(x5.accept(Eval()))
print(x5.accept(PrintPrefix()))
print(x5.accept(PrintPostfix()))