def top_k_frequent_words(words, k):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    
    candidates = sorted(
        count.items(),
        key=lambda item: (-item[1], item[0])
    )
    return [word for word, _ in candidates[:k]]


# 测试代码
test_words = ["i", "love", "leetcode", "i", "love", "coding"]
test_k = 2
print(top_k_frequent_words(test_words, test_k))