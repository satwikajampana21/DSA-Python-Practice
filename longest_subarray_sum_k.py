def longest_subarray_sum_k(arr, k):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        if current_sum == k:
            max_length = max(max_length, right - left + 1)

    return max_length


arr = [1, 2, 1, 1, 1, 1, 2, 3]
k = 3
print("Longest Subarray Length:", longest_subarray_sum_k(arr, k))
