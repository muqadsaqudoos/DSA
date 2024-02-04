def sum_of_list_by_recursion(arr):
    if len(arr) == 1:
        return arr[0]

    arr[1] = arr[0]+arr[1]
    
    return sum_of_list_by_recursion(arr[1:])
    
a = [18,7,3,6,9,3,5,4,8,0,4,5,7,8]
print(sum_of_list_by_recursion(a))
    
    
    
    
