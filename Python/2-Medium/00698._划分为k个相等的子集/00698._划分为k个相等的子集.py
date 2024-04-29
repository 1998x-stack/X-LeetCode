def can_partition_k_subsets(nums, k):
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False
    
    target = total_sum // k
    nums.sort(reverse=True)
    used = [False] * len(nums)
    
    def backtrack(start, bucket_sum, count):
        if count == k:
            return True
        if bucket_sum == target:
            return backtrack(0, 0, count + 1)
        for i in range(start, len(nums)):
                if used[i] or bucket_sum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(i + 1, bucket_sum + nums[i], count):
                    return True
                used[i] = False
                if bucket_sum == 0:
                    break
        return False
    
    return backtrack(0, 0, 0)


# Testing various edge cases
test_cases = [
    ([], 1),
    ([1, 2, 3], 1),
    ([1, 2, 3], 3),
    ([1, 1, 1, 1], 4),
    ([2, 2, 2, 2, 2], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),
    ([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5], 4),
    ([1], 2)
]

for nums, k in test_cases:
    result = can_partition_k_subsets(nums, k)
    print(f"Test case nums={nums}, k={k}, result={result}")