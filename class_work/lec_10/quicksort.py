def partition(a,low,high):
    x = a[high]
    i = low-1
    for j in range(low,high):
        if a[j] < x:
            i+=1
            a[j], a[i] = a[i], a[j]
    a[i+1], a[high] = a[high], a[i+1]
    return i +1

def quickSort(A, low,high):
    if low<high:
        q = partition(A, low, high)
        quickSort(A, low, q-1)
        quickSort(A, q+1, high)



        
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:", arr)