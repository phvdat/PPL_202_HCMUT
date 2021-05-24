# bai 1
def lessThan(list,n):
    return [x for x in list if x <n ]
# bai 2
def lstSquare(n):
    return [x*x for x in range(1,n+1)]
# bai 3
def lstSquare(n):
    if n == 1:
        return [1]
    else: return lstSquare(n-1) +[n*n]
# bai 4
def flatten(lst):
    if(len(lst)==0):
        return []
    else:
        return flatten(lst[0:-1]) +lst[-1]
# bai 5
def dist(lst,n):
    if(len(lst)==0):
        return []
    else:
        return [(lst[0],n)]+ dist(lst[1:],n)
# bai 6
def lessThan(lst,n):
    return list(filter(lambda x : x < n,lst))
# bai 7
def dist(lst,n):
    return list(map(lambda x: (x,n), lst))
# bai 8
from functools import reduce
def flatten(lst):
    return reduce(lambda prev, curr: prev+curr, lst, [])
# bai 9
def powGen(x):
    def f(y):
        return y**x
    return f
# bai 10
def increase(x):
    return x+1
def square(x):
    return x*x
def compose(*g):
    def h(args):
        return reduce(lambda x,y: y(x), reversed(g), args)
    return h
f = compose(increase,square)
print(f(3)) #increase(square(3)) = 10