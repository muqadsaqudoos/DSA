def isSorted(lst, size):
    if size == 0 or size == 1:
        return True
    
    if lst[0] > lst[1]:
        return False
    else:
        ans = isSorted(lst[1:], size - 1)
        return ans

a = [1,2,3,4,5]
b = isSorted(a, 5)
if b:
    print("list is sorted")
else:
    print("list is not sorted")
