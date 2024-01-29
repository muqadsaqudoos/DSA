def sayDigit(n, lsit):
    if (n==0):
        return 
    digit = n%10
    n = n//10
    
    sayDigit(n, list)
    print(list[digit],end=" ")

list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
n = int(input("Enter no: "))
sayDigit(n, list)