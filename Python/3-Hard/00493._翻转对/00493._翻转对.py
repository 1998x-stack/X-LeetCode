from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        计算数组中的翻转对数量。
        
        Args:
        nums: List[int] 输入的整数数组。
        
        Returns:
        int: 数组中的翻转对数量。
        
        """
        # 归并排序并计算翻转对
        def mergeSort(nums, left, right):
            # 如果左边界不小于右边界，不需要处理
            if left >= right:
                return 0
            
            # 分治法的中点
            mid = (left + right) // 2
            # 递归计算左半部分和右半部分的翻转对数量
            count = mergeSort(nums, left, mid) + mergeSort(nums, mid + 1, right)
            
            # 归并排序的同时计算当前分段的翻转对数量
            # j用于寻找满足翻转对条件的右半部分的索引
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # 合并两个有序数组
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
            
            # 将排序后的数组复制回原数组
            for i in range(len(temp)):
                nums[left + i] = temp[i]
                
            return count
        
        return mergeSort(nums, 0, len(nums) - 1)

# 测试代码
solution = Solution()
test_cases = [
    ([1,3,2,3,1], 2),
    ([2,4,3,5,1], 3)
]

# 运行测试用例
for nums, expected in test_cases:
    result = solution.reversePairs(nums)
    print(f"nums: {nums}, expected: {expected}, result: {result}")
