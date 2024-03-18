from typing import List, Dict, Tuple

def group_shifted_strings(strings: List[str]) -> List[List[str]]:
    """
    将字符串数组进行分组，每个组内的字符串可以通过相同量的字符移动转换成彼此。
    
    参数:
        strings (List[str]): 输入的字符串数组。
        
    返回:
        List[List[str]]: 分组后的字符串数组。
        
    示例:
        输入: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
        输出: [["abc","bcd","xyz"], ["acef"], ["a","z"], ["az","ba"]]
    """
    
    # 初始化字典来存储分组结果，键是组标识符（元组），值是字符串列表
    groups: Dict[Tuple[int, ...], List[str]] = {}
    
    for string in strings:
        if not string:  # 空字符串的处理
            continue
        
        # 计算每个字符串的“组键”，即每个字符与第一个字符的差值序列
        # 利用ord函数计算字符的ASCII码值，以便进行差值计算
        key = tuple((ord(char) - ord(string[0])) % 26 for char in string)
        
        # 将字符串添加到对应的分组中
        if key not in groups:
            groups[key] = [string]
        else:
            groups[key].append(string)
    
    # 将字典中的值转换为列表，得到最终的分组结果
    return list(groups.values())

# 测试代码
test_strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
grouped_strings = group_shifted_strings(test_strings)
for group in grouped_strings:
    print(group)