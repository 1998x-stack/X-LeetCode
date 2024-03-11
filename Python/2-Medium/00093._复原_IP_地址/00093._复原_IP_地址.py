from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 存储结果的列表
        result = []
        
        # 递归搜索函数
        def backtrack(start, path):
            # 达到四个整数且字符串已经遍历完
            if start == len(s) and len(path) == 4:
                result.append('.'.join(path))
                return
            
            # 尝试分割下一个整数
            for i in range(1, 4):
                # 分割的整数不越界
                if start + i <= len(s):
                    # 取出当前整数
                    num_str = s[start:start+i]
                    # 判断整数是否在有效范围
                    if 0 <= int(num_str) <= 255 and (num_str[0] != '0' or len(num_str) == 1):
                        # 递归搜索下一个整数
                        backtrack(start + i, path + [num_str])
        
        # 调用递归函数
        backtrack(0, [])
        return result

# 测试代码
solution = Solution()
result = solution.restoreIpAddresses("25525511135")
print(result)