import random
import time

def counting_sort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)

    for num in arr:
        counts[num] += 1

    sorted_arr = []
    for i in range(len(counts)):
        sorted_arr+= [i]*counts[i]

    return sorted_arr

random_numbers = [random.randint(0, 10000) for _ in range(5000)]


start_time = time.time()
counting_sort(random_numbers)
end_time = time.time()
counting_time = end_time - start_time

print("Time taken to sort using counting sort:", counting_time, "seconds")
