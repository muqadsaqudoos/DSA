def array_sum(arr,key):
    if key < arr[0] and key > (arr[-1]*2):
        return False
    return sum_recursion(arr,key,0,len(arr)-1)

def sum_recursion(arr,key,i,j):
    if i == j :
        return False
    elif arr[i]+arr[j] == key :
        return True
    elif arr[i]+arr[j] > key:
        return sum_recursion(arr,key,i,j-1)
    else:
        return sum_recursion(arr,key,i+1,j)

arr = [1,3,5,7,9]
print(array_sum(arr,15))