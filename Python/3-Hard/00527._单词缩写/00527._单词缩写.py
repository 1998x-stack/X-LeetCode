from typing import List, Dict

def abbreviate(words: List[str]) -> List[str]:
    """
    对给定的单词列表进行唯一缩写。
    
    Args:
    words: List[str] - 输入的单词列表。
    
    Returns:
    List[str] - 缩写后的单词列表，保证唯一性。
    
    示例:
    >>> abbreviate(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"])
    ['l2e', 'god', 'internal', 'me', 'internet', 'interval', 'int4n', 'face', 'intr4n']
    """
    
    # 如果单词长度小于等于3，直接返回原单词；否则返回缩写形式
    def abbreviate_word(word: str) -> str:
        return word if len(word) <= 3 else f"{word[0]}{len(word)-2}{word[-1]}"
    
    # 初始化：存储每个缩写对应的单词列表
    abbrev_map: Dict[str, List[str]] = {}
    for word in words:
        abbr = abbreviate_word(word)
        if abbr not in abbrev_map:
            abbrev_map[abbr] = []
        abbrev_map[abbr].append(word)
    
    # 存储最终结果的列表
    result: List[str] = []
    
    # 遍历每个单词，处理冲突的缩写
    for word in words:
        abbr = abbreviate_word(word)
        # 如果这个缩写是唯一的，直接添加到结果列表
        if len(abbrev_map[abbr]) == 1:
            result.append(abbr)
        else:
            # 处理缩写冲突，逐渐增加缩写中的字母数量，直到缩写唯一
            for i in range(1, len(word)-2):
                abbr = f"{word[0]}{i}{word[i+1:-1]}{word[-1]}"
                if abbr not in abbrev_map:
                    abbrev_map[abbr] = [word]
                    result.append(abbr)
                    break
                elif word in abbrev_map[abbr]:
                    result.append(abbr)
                    break
    
    return result

# 测试代码
test_words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
abbreviated_words = abbreviate(test_words)
abbreviated_words