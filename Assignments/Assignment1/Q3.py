def binary_search_recursion(arr,s,e,key):
    
    if s > e :
        return False
    
    mid = (s+e)//2

    if arr[mid] == key:
        return True
    
    elif arr[mid] < key:
        return binary_search_recursion(arr,mid+1,e,key)
    
    else:
        return binary_search_recursion(arr,s,mid-1,key)

arr = [1,4,7,8,78,90]
key = 2
b = binary_search_recursion(arr,0,len(arr)-1,key)
if b :
    print(f"{key} is in list")

else:
    print(f"{key} is not in list")