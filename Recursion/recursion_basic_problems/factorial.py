def factorial(n):
    if (n==0):
        return 1
    
    smallerProblem = factorial(n-1)
    biggerProblem = n*smallerProblem
    return biggerProblem

a = int(input("Enter number: "))
print(factorial(a))