def reverse_string(s):
    if len(s) <= 1:
        return s
    print(s)
    a = reverse_string(s[1:]) + s[0]
    print(a)
    return a

original_str = "abcde"
print()
reverse_string(original_str)
