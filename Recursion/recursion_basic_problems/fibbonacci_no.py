def fib(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    ans = fib(n-1)+fib(n-2)

    return ans

n = int(input("enter the nth fibbanaci no: "))
print(fib(n))
    
