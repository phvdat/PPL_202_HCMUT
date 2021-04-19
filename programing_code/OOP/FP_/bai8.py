from functools import reduce
def flatten(lst):
    return reduce(lambda prev, curr: prev+curr, lst, [])
print(flatten([[1,2,3],[4,5],[6,7]])
)