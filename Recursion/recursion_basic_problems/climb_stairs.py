def climb(n):
    if (n<0):
        return 0
    
    if (n==0):
        return 1
    
    ans = climb(n-1) + climb(n-2)
    return ans

a = int(input("Enter n: "))
print(climb(a))