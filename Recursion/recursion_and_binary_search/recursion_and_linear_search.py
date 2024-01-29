def linearSearch(arr,size,value):
    if size == 0:
        return False
    
    if arr[0]==value:
        return True
    else:
        remianingPart = linearSearch(arr[1:],size-1,value)
        return remianingPart
    
a = [1,2,3,4,5,6]
b = linearSearch(a,6,4)
if b:
    print("present")
else:
    print("absent")
    