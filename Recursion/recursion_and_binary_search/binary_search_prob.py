def binarySearch(list,size,value):
    start = 0
    end = size-1
    mid = (start+end)//2
    while start<=end:
        if list[mid] == value:
            return mid
        if list[mid]<value:
            start = mid+1

        else:
            end = mid -1
        mid = (start+end)//2

    return -1

list = [13,15,98,100,105]
print(binarySearch(list,5,78))