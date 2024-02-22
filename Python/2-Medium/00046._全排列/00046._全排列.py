from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        生成给定数组的所有全排列。

        参数:
        nums: List[int] -- 不含重复数字的整数数组。

        返回:
        List[List[int]] -- 数组的所有全排列。

        示例:
        >>> permute([1,2,3])
        [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        """
        def backtrack(path, options):
            # 如果选项为空，说明找到了一种排列
            if not options:
                result.append(path[:])  # 使用 path[:] 来复制路径，避免后续修改
                return
            # 遍历当前可选的数字
            for i in range(len(options)):
                # 选择当前数字
                path.append(options[i])
                # 递归调用，注意传递新的可选项列表（排除已选的数字）
                backtrack(path, options[:i] + options[i+1:])
                # 回溯，撤销选择
                path.pop()

        result = []
        backtrack([], nums)
        return result

# 创建 Solution 实例
sol = Solution()
# 测试用例
test_nums = [1, 2, 3]
# 获取全排列结果
result = sol.permute(test_nums)
# 打印结果
print(result)