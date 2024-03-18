from typing import List

def shortest_word_distance(words: List[str], word1: str, word2: str) -> int:
    """
    寻找列表中两个单词之间的最短距离。如果两个单词相同，则计算同一单词的两个实例之间的最短距离。

    Args:
    words: 字符串列表，代表单词列表。
    word1: 字符串，需要计算距离的第一个单词。
    word2: 字符串，需要计算距离的第二个单词。

    Returns:
    int: word1 和 word2 之间的最短距离。

    示例:
    >>> shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")
    1
    >>> shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes")
    3
    """
    index1, index2 = -1, -1  # 初始化两个词的最近出现位置
    min_distance = float('inf')  # 初始化最短距离为正无穷大
    same_word = word1 == word2  # 检查两个词是否相同

    for i, word in enumerate(words):
        if same_word and word == word1:  # 如果两个词相同
            if index1 > -1:  # 确保不是第一次遇到这个词
                min_distance = min(min_distance, i - index1)
            index1 = i
        else:
            if word == word1:
                index1 = i
            if word == word2:
                index2 = i

            if index1 != -1 and index2 != -1:  # 确保两个词都至少出现过一次
                min_distance = min(min_distance, abs(index1 - index2))

    return min_distance

# 测试代码
test_cases = [
    (["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"),
    (["practice", "makes", "perfect", "coding", "makes"], "makes", "makes")
]

for words, word1, word2 in test_cases:
    print(f"words: {words}, word1: {word1}, word2: {word2} => shortest distance: {shortest_word_distance(words, word1, word2)}")