# # from functools import reduce

# # # def lessThan(lst, n):
# # #     return list(filter(lambda a: a<n,lst))
# # # def lessThan(lst, n):
# # #     if (len(lst) ==0):
# # #         return []
# # #     if (lst[0]<n):
# # #         return [lst[0]] + lessThan(lst[1:],n)
# # #     else:
# # #         return  lessThan(lst[1:],n)

# # # print(lessThan([7,6,4,4,5],4))

# # # Dệ quy
# # # def lstSquare(n):
# # #     if n==0:
# # #         return []
# # #     else:
# # #         return lstSquare(n-1) +[n*n]
# # # a = lstSquare(3)
# # # print(a)

# # # dung for
# # # def lstSquare(n):
# # #     res = []
# # #     for i in range(1,n+1):
# # #         print(i)
# # #         res+= [i*i]
# # #     return res

# # # a = lstSquare(3)
# # # print(a)

# # # def lstSquare(n):
# # #     return [x*x for x in range(1,n+1)]
# # # a = lstSquare(3)
# # # print(a)



# # # def flatten(lst):
# # #     if len(lst) ==0:
# # #         return []
# # #     else:
# # #         return lst[0] + flatten(lst[1:])
# # # def dist(lst, n):
# # #     if len(lst) == 0:
# # #         return []
# # #     else:
# # #         return [(lst[0],n)]+ dist(lst[1:],n)
# # # def dist(lst, n):
# # #     return list(map(lambda x: (x,n),lst))

# # # def lessThan(lst, n):
# # #     return list(filter(lambda x: x<n, lst))
# # # a  = lessThan([1,2,3,-1,0],4)
# # # print(a)

# # # def dist(lst, n):
# # #     return list(map(lambda x : (x, n), lst))


# # def flatten(lst):
# #     return reduce(lambda x,y: x+y, lst, [])
# # a  = flatten([[1,2,3],[4,5],[6,7]])
# # print(a)

# # def powGen(x):
# #     def f(y):
# #         return y**x
# #     return f
# # square = powGen(2)
# # print(square(4))

# # def compose(*g):
# #     def f(x):
# #         return reduce( lambda a,b: b(a), reversed(g),x)
# #     return f
# # def increase(x):
# #     return x+1
# # def square(x):
# #     return x*x
# # f = compose(increase,square)
# # print(f(3)) #increase(square(3)) = 10



# # class Exp(): pass
# # class IntLit(Exp):
# #     def __init__(self, value):
# #         self.value = value
# #     def eval(self):
# #         return self.value
# # class FloatLit(Exp):
# #     def __init__(self, value):
# #         self.value = value
# #     def eval(self):
# #         return self.value
# # class BinExp(Exp):
# #     def __init__(self, op1, op, op2):
# #         self.op1 = op1
# #         self.op = op
# #         self.op2 = op2
# #     def eval(self):
# #         value1 = self.op1.eval() #vi k biet tham so la gi , intlit
# #         value2 = self.op2.eval()
# #         if self.op=='+':
# #             return value1 + value2
# #         elif self.op=='-':
# #             return value1 - value2
# #         elif self.op=='*':
# #             return value1 * value2
# #         elif self.op=='/':
# #             return value1 / value2

# # class UnExp(Exp):
# #     def __init__(self, op1, op2):
# #         self.op1 = op1
# #         self.op2 = op2
# #     def eval(self):
# #         value = self.op2.eval()

# #         if self.op1=='-':
# #             return -value
# #         elif self.op1=='+':
# #             return value
# # x1 = IntLit(1)
# # print(x1.eval())




# class Exp():
#     def printValue(self):
#         return self.value
# class IntLit(Exp):
#     def __init__(self, value):
#         self.value = value
#     def eval(self):
#         return self.value
# class FloatLit(Exp):
#     def __init__(self, value):
#         self.value = value
#     def eval(self):
#         return self.value

# class BinExp(Exp):
#     def __init__(self, op1, op, op2):
#         self.op1 = op1
#         self.op = op
#         self.op2 = op2
#     def eval(self):
#         val1 = self.op1.eval()
#         val2 = self.op2.eval()
#         if op == '+':
#             return op1+op2
#         if op == '*':
#             return op1*op2
#         if op == '/':
#             return op1/op2
#         if op == '-':
#             return op1-op2
#     def printValue(self):
#         return self.op + self.op1.printValue() +  self.op1.printValue()
# class UnExp(Exp):
#     def __init__(self, op1, op2):
#         self.op1 = op1
#         self.op2 = op2
#     def eval(self):
#         val = self.op2.eval()
#         if op1 == '+':
#             return op2
#         if op1 == '-':  
#             return -op2
#         def printValue(self):
#             return self.op + self.op2.printValue()
# x3 = BinExp(IntLit(1), '+',IntLit(4)) 
	
# print(x3.printValue())

a =5
print(type(a))