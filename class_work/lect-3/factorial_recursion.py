def fact_recursion(n):
    if n == 1:
        return 1
    
    return n * fact_recursion(n-1)


print(fact_recursion(10))