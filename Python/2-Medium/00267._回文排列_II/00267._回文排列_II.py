from typing import List, Dict

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        """
        生成给定字符串的所有唯一的回文排列。
        
        Args:
        s: 字符串。
        
        Returns:
        一个包含所有唯一回文排列的列表。
        
        """
        # 统计字符出现的频率
        freq = {}  # type: Dict[str, int]
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            
        # 检查回文排列可能性
        odd_count = sum(1 for count in freq.values() if count % 2 == 1)
        if odd_count > 1:
            return []  # 不能形成回文排列
        
        # 构建回文排列的一半
        half = []
        mid = ""
        for char, count in freq.items():
            if count % 2 == 1:
                mid = char
                count -= 1
            half.extend([char] * (count // 2))
            
        # 生成所有唯一的排列
        results = []
        self.backtrack(half, 0, mid, results)
        return results
    
    def backtrack(self, arr: List[str], index: int, mid: str, results: List[str]):
        """
        使用回溯法生成所有唯一的排列。
        
        Args:
        arr: 构建回文的一半字符列表。
        index: 当前处理的索引。
        mid: 中心字符。
        results: 存储结果的列表。
        
        """
        if index == len(arr):
            # 生成完整的回文字符串并添加到结果列表中
            half_palindrome = ''.join(arr)
            results.append(half_palindrome + mid + half_palindrome[::-1])
            return
        
        seen = set()
        for i in range(index, len(arr)):
            if arr[i] in seen:
                continue  # 避免重复的排列
            seen.add(arr[i])
            arr[index], arr[i] = arr[i], arr[index]
            self.backtrack(arr, index + 1, mid, results)
            arr[index], arr[i] = arr[i], arr[index]  # 回溯
        
# 测试代码
solution = Solution()
test_str = "aabb"
print(solution.generatePalindromes(test_str))