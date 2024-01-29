def binarySearch(arr,start,end,value):
    if start>end:
        return False
    mid = (start+end)//2
    if arr[mid] == value:
        return True
    if arr[mid]<value:
        a = binarySearch(arr,mid+1,end,value)
        return a
    else:
        a = binarySearch(arr,start,mid-1,value)
        return a
        
list = [13,15,98,100,105]
print(binarySearch(list,0,5,13))