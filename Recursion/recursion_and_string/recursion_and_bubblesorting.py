def bubbleSort(arr,size):
    if (size == 0 or size == 1):
        return 
    for i in range(size-1):
        if arr[i]>arr[i+1]:
            arr[i] , arr[i+1] = arr[i+1] , arr[i]
    
    bubbleSort(arr,size-1)
a = [1,4,62,4,7]
bubbleSort(a,5)
for i in range(5):
    print(a[i],end = " ")