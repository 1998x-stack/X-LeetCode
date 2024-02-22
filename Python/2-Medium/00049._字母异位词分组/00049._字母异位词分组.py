from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    将字符串数组按字母异位词分组。
    
    Args:
    strs: List[str] 输入的字符串数组。
    
    Returns:
    List[List[str]] 分组后的字母异位词数组。
    
    示例:
    输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出: [["ate","eat","tea"], ["nat","tan"], ["bat"]]
    """
    # 使用哈希表存储分组，键是排序后的字符串
    anagrams = defaultdict(list)
    
    # 遍历输入的字符串数组
    for s in strs:
        # 对每个字符串排序，并将排序后的字符串作为键，原字符串添加到对应的列表中
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)
        
    # 收集哈希表中的所有值作为结果输出
    return list(anagrams.values())

# 示例数据
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 运行代码
result = groupAnagrams(strs)
# 打印结果
print(result)