def next_permutation(nums):
    """
    实现寻找给定整数数组的下一个排列的函数。
    
    Args:
    nums (List[int]): 整数数组
    
    Returns:
    None: 原地修改数组，不返回值。
    
    Examples:
    >>> nums = [1, 2, 3]
    >>> next_permutation(nums)
    >>> print(nums)
    [1, 3, 2]
    
    >>> nums = [3, 2, 1]
    >>> next_permutation(nums)
    >>> print(nums)
    [1, 2, 3]
    
    >>> nums = [1, 1, 5]
    >>> next_permutation(nums)
    >>> print(nums)
    [1, 5, 1]
    """
    def reverse(nums, start):
        """
        将数组从start位置到末尾的部分进行反转。
        
        Args:
        nums (List[int]): 整数数组
        start (int): 开始反转的位置
        
        Returns:
        None: 原地修改数组，不返回值。
        """
        i, j = start, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    
    # 从后向前查找第一个升序的相邻元素对(i, i+1)
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # 从数组末尾开始向前查找第一个大于nums[i]的元素nums[j]
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        # 交换nums[i]和nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    
    # 反转i+1到数组末尾的部分
    reverse(nums, i + 1)

# 测试代码
nums_list = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 1, 5],
    [1, 3, 2]
]

# 对每个测试用例应用next_permutation函数并打印结果
for nums in nums_list:
    next_permutation(nums)
    print(nums)