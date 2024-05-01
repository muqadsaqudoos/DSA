def isSorted(arr):
    if arr[0]<arr[1]:
        if len(arr) == 2:
            return True
        return isSorted(arr[1:])
    return False


a = [1,3,6,8]
print(isSorted(a))


