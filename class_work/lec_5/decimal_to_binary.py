def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return decimal_to_binary(n//2) + str(n%2)
    
    
print(decimal_to_binary(10))
    
