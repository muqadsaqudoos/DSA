class binarySearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, s, e, n):
        mid = (s + e) // 2
        
        if s > e:
            return False
        
        if self.arr[mid] == n:
            return True
        
        if n > self.arr[mid]:
            return self.search(mid + 1, e, n)
        else:
            return self.search(s, mid - 1, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bs = binarySearch(arr)
result = bs.search(0, len(arr) - 1, 5)
if result:
    print(f"element in array")

else:
    print(f"element not in array")
