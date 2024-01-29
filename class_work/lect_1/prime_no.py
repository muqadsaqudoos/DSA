def isprimeNo(a):
    for i in range(2,a):
        if a%i == 0:
            return False
    return True

a = 10
i = 0
b = 2
while i < a:
    if isprimeNo(b):
        print(f"{b} is a prime no")
        i += 1   
    b += 1