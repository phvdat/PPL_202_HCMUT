def powGen(x):
    def f(y):
        return x**y
    return f

square = powGen(2)
print(square(4))