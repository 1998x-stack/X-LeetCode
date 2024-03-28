from typing import List


class Solution:
    """
    计算屏幕可容纳的句子数量
    """

    def words_fitting(self, rows: int, cols: int, sentence: List[str]) -> int:
        """
        计算屏幕可容纳的句子数量

        参数:
            rows (int): 屏幕行数
            cols (int): 屏幕列数
            sentence (List[str]): 句子单词列表

        返回:
            int: 句子在屏幕上完整显示的次数
        """

        n = len(sentence)
        # dp[i] 表示前 i 个单词能否放入前 i 行
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            cur_len = 0  # 当前行单词总长度
            for j in range(i):
                # 检查单词长度是否超出当前行剩余空间
                if len(sentence[j]) > cols - cur_len:
                    break
                cur_len += len(sentence[j]) + 1  # 加上空格长度
                # 之前单词能放入前 i - 1 行，当前单词能放入当前行
                if dp[j] and cur_len <= cols:
                    dp[i] = True
                    break

        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    rows = 2
    cols = 8
    sentence = ["hello", "world"]
    result = solution.words_fitting(rows, cols, sentence)
    print(f"句子在屏幕上完整显示的次数: {result}")
