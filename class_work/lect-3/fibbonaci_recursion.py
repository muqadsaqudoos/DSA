# we are finding the nth fibonacci number

def fibb_recursion(n):
    # we are taking 1 as 1st fibbnoaci number
    # if you want to take 0 as 1st fibbboaci bas case will be if n == 1: return 0; if n == 2: return 1
    if n == 0 :
        return 0
    
    if n == 1 :
        return 1
    
    return fibb_recursion(n-1) + fibb_recursion(n-2)


print(fibb_recursion(4))

