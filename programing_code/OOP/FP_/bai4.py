def flatten(lst):
    if(len(lst)==0):
        return []
    else:
        return flatten(lst[0:-1] +lst[-1])
        # return flatten(lst[0:len(lst)-1] +lst[-1])
        # print*lst[0:1]
print(flatten([[1,2,3],[4,5],[6,7]]))