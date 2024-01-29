
def sum1(list,size):
    if (size==0):
        return 0
    if (size==1):
        return list[0]
    ans = sum1(list[1:],size-1)
    sum = list[0] + ans
    return sum
    

a = [1,2,3,4,5]
print(sum1(a,5))