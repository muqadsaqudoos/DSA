def count(n):
    if (n==0):
        return
    
    print(n)
    count(n-1)

n = int(input("Enter no: "))
count(n)        