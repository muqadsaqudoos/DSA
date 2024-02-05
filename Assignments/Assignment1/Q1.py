def is_palindrom_by_recursion(string,s,e):
    if s > e :
        return True
    if string[s] == string[e]:
        return is_palindrom_by_recursion(string,s+1,e-1)
    
    else:
        return False
    
a = "abba"
b = is_palindrom_by_recursion(a,0,3)
if b:
    print(f"{a} is Palindrom")

else:
    print(f"{a} is not Palindrom")