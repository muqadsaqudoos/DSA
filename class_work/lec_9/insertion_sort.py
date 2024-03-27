def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr


a = [0,9,4,3,11,15,2,5,8,3,1,9,100,-1]
print(insertion_sort(a))
