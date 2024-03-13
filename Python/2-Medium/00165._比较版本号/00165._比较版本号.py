from typing import List

def split_and_normalize(version: str) -> List[int]:
    """
    分割并标准化版本号字符串。
    
    Args:
        version: 一个版本号字符串。
        
    Returns:
        一个整数列表，表示标准化后的版本号各段。
    
    说明:
        - 分割字符串，使用'.'作为分隔符。
        - 转换每段为整数，以去除前导零。
    """
    return [int(v) for v in version.split('.')]

def compare_version(version1: str, version2: str) -> int:
    """
    比较两个版本号。
    
    Args:
        version1: 第一个版本号字符串。
        version2: 第二个版本号字符串。
        
    Returns:
        - 如果version1 > version2，返回1。
        - 如果version1 < version2，返回-1。
        - 否则，返回0。
        
    说明:
        - 首先分割并标准化两个版本号。
        - 然后逐段比较，直到找到差异或遍历完所有段。
    """
    v1 = split_and_normalize(version1)
    v2 = split_and_normalize(version2)
    len_v1, len_v2 = len(v1), len(v2)
    
    for i in range(max(len_v1, len_v2)):
        num1 = v1[i] if i < len_v1 else 0
        num2 = v2[i] if i < len_v2 else 0
        
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
            
    return 0  # 所有段都相等

# 示例运行
results = {
    "1.01 vs 1.001": compare_version("1.01", "1.001"),  # 应该输出: 0
    "1.0 vs 1.0.0": compare_version("1.0", "1.0.0"),    # 应该输出: 0
    "0.1 vs 1.1": compare_version("0.1", "1.1")         # 应该输出: -1
}
print(results)