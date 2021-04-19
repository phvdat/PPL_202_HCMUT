# bai1
def lessThan(lst,n):
    return list(filter(lambda x: x<n, lst))
    # return [x for x in lst if x < n]

# bai 2
def lstSquare(n):
    # lst = range(1,n+1)
    # return list(map(lambda x: x*x, lst))
    return [x*x for x in range(1, n+1)]

# bai 3
def lstSquare(n):
    if n==1:
        return [1]
    else:
        return lstSquare(n-1) + [n*n]

# bai 4 
def flatten(lst):
    if len(lst) ==0:
        return []
    else:
        return lst[0] + flatten(lst[1:])

# bai 5
def dist(lst,n):
    # return list(map(lambda x: (x,n), lst))
    if len(lst) == 0:
        return []
    else:
        # return [(x, n) for x in lst]
        return [(lst[0], n)] + dist(lst[1:],n)

# bai 6 higt-order function
def lessThan(lst,n):
    # return [x for x in lst if x<n]
    return list(filter(lambda x: x<n, lst))

# abai7 high - order function


# bai 8 high- order function
from functools import reduce
def flatten(lst):
    return reduce(lambda x, y: x+y, lst,[])


# bai 9
def powGen(x):
    def f(y):
        return y**x
    return f
# square = powGen(2)
# print(square(4))

# bai 10
def increase(x):
    return x+1
def square(x):
    return x*x
def double(x):
    return x*2
def compose(*g):
    def h(f):
        print(list(g))
        return reduce(lambda x, y: y(x), reversed(g), f)
    return h
f = compose(increase,square,double)
print(f(3))