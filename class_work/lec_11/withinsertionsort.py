import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

random_numbers = [random.randint(0, 10000) for _ in range(5000)]
start_time = time.time()
insertion_sort(random_numbers)
end_time = time.time()

time_taken = end_time - start_time

print("Time taken to sort using insertion sort:", time_taken, "seconds")
