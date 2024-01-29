def isPalindrom(s):
    if len(s)<=1:
        return True
    
    if s[0]!=s[-1]:
        return False
    print(s)
    a =  isPalindrom(s[1:-1])
    return a
palindrome_str = "radar"
non_palindrome_str = "hello"

print(f"Is '{palindrome_str}' a palindrome? {isPalindrom(palindrome_str)}")
