def reverse_string_recursion(string):
    if len(string) == 1:
        return string
    return reverse_string_recursion(string[1:])+string[0]


a = "hahahahha"
print(reverse_string_recursion(a))