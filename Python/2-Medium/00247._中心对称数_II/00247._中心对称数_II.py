from typing import List

def findStrobogrammatic(n: int) -> List[str]:
    """
    生成所有长度为n的中心对称数。
    
    Args:
    n: 目标中心对称数的长度
    
    Returns:
    一个包含所有长度为n的中心对称数的列表。
    """
    def buildStrobogrammatic(length: int, n: int) -> List[str]:
        """
        递归构建中心对称数。
        
        Args:
        length: 当前构建的中心对称数的目标长度。
        n: 最终的目标长度。
        
        Returns:
        一个包含所有长度为length的中心对称数的列表。
        """
        if length == 0: return ['']  # 空字符串是长度为0的中心对称数
        if length == 1: return ['0', '1', '8']  # 长度为1时的中心对称数
        
        middles = buildStrobogrammatic(length - 2, n)  # 递归构建中间部分
        
        result = []
        for middle in middles:
            if length != n:  # 非最外层可以添加'0' '0'
                result.append('0' + middle + '0')
            result.append('1' + middle + '1')
            result.append('8' + middle + '8')
            result.append('6' + middle + '9')
            result.append('9' + middle + '6')
        return result
    
    return buildStrobogrammatic(n, n)

# 测试代码
n = 2
strobogrammatic_numbers = findStrobogrammatic(n)
print(f"长度为 {n} 的中心对称数有：{strobogrammatic_numbers}")