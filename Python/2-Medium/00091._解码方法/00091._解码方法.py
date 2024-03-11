from typing import List

def num_decodings(s: str) -> int:
    # Step 1: 初始化dp数组，长度为字符串长度加1，初始值为0
    n = len(s)
    dp = [0] * (n + 1)
    
    # Step 2: 设置dp[0] = 1，因为空字符串只有一种解码方式
    dp[0] = 1
    
    # Step 3: 遍历字符串，根据递推关系更新dp数组
    for i in range(1, n + 1):
        # 如果当前字符不是'0'，则可以单独解码当前字符
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        # 如果前一个字符和当前字符组成的数字在1到26之间，则可以组合解码
        if i > 1 and 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    
    # Step 4: 最终dp数组的最后一个元素即为总的解码方法数
    return dp[n]

# Example usage
input_str = "226"
result = num_decodings(input_str)
print(f"The number of decoding methods for '{input_str}' is: {result}")