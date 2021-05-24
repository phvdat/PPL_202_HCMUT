newlist = []
def lstSquare(n):
    if n == 1:
        return [1]
    else: return lstSquare(n-1) +[n*n]