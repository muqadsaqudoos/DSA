def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

a = [0,9,4,3,11,15,2,5,8,3,1,9,100,-1]
print(bubble_sort(a))