def b_s(arr,element):
    low,high = 0,len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]<element:
            low = mid+1
        elif arr[mid]>element:
            high = mid-1
        else:
            return arr[mid]
    return -1
        
arr1 = [13, 27, 35, 40, 49, 55, 59]
arr2 = [17, 35, 39, 40, 55, 58, 60]

for element in arr1:
    if b_s(arr2,element) == element:
        print(element)