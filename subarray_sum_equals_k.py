def subarray_sum_equals_k(arr, k):
    prefix_sum = 0
    count = 0
    hashmap = {0: 1}

    for num in arr:
        prefix_sum += num

        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum - k]

        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count


arr = [1, 1, 1]
k = 2
print("Number of Subarrays:", subarray_sum_equals_k(arr, k))
