from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        根据输入的数字字符串，返回所有可能的字母组合。

        Args:
        digits: str - 一个仅包含数字2-9的字符串。

        Returns:
        List[str] - 可能的字母组合列表。

        示例:
        >>> solution = Solution()
        >>> solution.letterCombinations("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        """
        # 数字到字母的映射
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(combination: str, next_digits: str) -> None:
            """使用回溯法生成所有可能的字母组合"""
            # 如果没有更多的数字需要检查
            if len(next_digits) == 0:
                # 已经处理完所有数字，当前组合是最终结果之一
                combinations.append(combination)
            else:
                # 遍历当前数字对应的所有可能的字母
                for letter in phone_map[next_digits[0]]:
                    # 递归调用，将当前字母加到已有组合上，并处理下一个数字
                    backtrack(combination + letter, next_digits[1:])

        combinations = []
        if digits:
            backtrack("", digits)
        return combinations

# 实例化Solution类，并测试功能
solution = Solution()
test_digits = "23"
print(f"输入数字字符串: {test_digits}")
print("可能的字母组合:", solution.letterCombinations(test_digits))
