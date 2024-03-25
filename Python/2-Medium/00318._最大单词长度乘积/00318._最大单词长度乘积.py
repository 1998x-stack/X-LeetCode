from typing import List

def maxProduct(words: List[str]) -> int:
    """
    计算不包含相同字符的两个单词长度乘积的最大值。
    
    Args:
        words: 字符串列表，每个元素是一个单词。
    
    Returns:
        两个单词长度乘积的最大值。
        
    示例:
        >>> maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
        16
    """
    # 将单词转换为二进制表示，并记录其长度
    word_bits = {}  # key为单词的二进制表示，value为单词的长度
    for word in words:
        bits = 0
        for char in word:
            # 计算字符在字母表中的位置，并设置相应的位
            bits |= 1 << (ord(char) - ord('a'))
        # 记录单词的最大长度（相同二进制表示可能对应不同长度的单词）
        word_bits[bits] = max(word_bits.get(bits, 0), len(word))
    
    max_product = 0
    # 比较所有单词，寻找最大长度乘积
    for x in word_bits:
        for y in word_bits:
            if x & y == 0:  # 如果没有公共字母
                max_product = max(max_product, word_bits[x] * word_bits[y])
                
    return max_product

# 测试代码
test_cases = [
    ["abcw","baz","foo","bar","xtfn","abcdef"],
    ["a","ab","abc","d","cd","bcd","abcd"],
    ["a","aa","aaa","aaaa"]
]

results = [maxProduct(words) for words in test_cases]
print(results)