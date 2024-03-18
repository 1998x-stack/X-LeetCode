from typing import List, Dict

class WordDistance:
    """
    单词距离查询类

    属性:
        word_index (Dict[str, List[int]]): 存储每个单词及其在列表中的所有索引位置的字典。

    方法:
        __init__(self, wordsDict: List[str]): 构造函数，接收一个单词列表，并初始化 word_index 属性。
        shortest(self, word1: str, word2: str) -> int: 返回两个单词之间的最短距离。
    """
    def __init__(self, wordsDict: List[str]):
        """
        初始化 WordDistance 类的一个实例。
        
        参数:
            wordsDict (List[str]): 单词列表。
        """
        self.word_index = {}  # 初始化单词索引字典
        # 遍历单词列表，记录每个单词的索引位置
        for index, word in enumerate(wordsDict):
            if word not in self.word_index:
                self.word_index[word] = []
            self.word_index[word].append(index)
    
    def shortest(self, word1: str, word2: str) -> int:
        """
        返回两个单词之间的最短距离。
        
        参数:
            word1 (str): 第一个单词。
            word2 (str): 第二个单词。
        
        返回:
            int: word1 和 word2 之间的最短距离。
        """
        indexes1, indexes2 = self.word_index[word1], self.word_index[word2]
        i, j = 0, 0
        min_distance = float('inf')  # 初始化最短距离为无穷大
        
        # 使用双指针遍历两个单词的索引列表
        while i < len(indexes1) and j < len(indexes2):
            min_distance = min(min_distance, abs(indexes1[i] - indexes2[j]))
            # 移动指针，总是尝试减小索引差
            if indexes1[i] < indexes2[j]:
                i += 1
            else:
                j += 1
        
        return min_distance  # 返回计算得到的最短距离

# 测试代码
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
wordDistance = WordDistance(wordsDict)
# 查询 "coding" 和 "practice" 之间的最短距离
print(wordDistance.shortest("coding", "practice"))  # 应返回 3
# 查询 "makes" 和 "coding" 之间的最短距离
print(wordDistance.shortest("makes", "coding"))  # 应返回 1