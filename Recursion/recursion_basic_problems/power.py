def power(n):
    if (n==0):
        return 1
    
    smallerProblem = power(n-1)
    biggerProblem = 2*smallerProblem
    return biggerProblem

n = int(input("Enter no: "))
print(power(n))