from typing import List

class Codec:
    def __init__(self):
        self.delimiter = '|'  # 选择一个不常用的字符作为分隔符

    def encode(self, strs: List[str]) -> str:
        """将字符串列表编码成一个字符串

        Args:
            strs: 待编码的字符串列表

        Returns:
            编码后的字符串

        通过在每个字符串前加上长度前缀和特殊分隔符来进行编码。
        """
        encoded = ''
        for s in strs:
            # 字符串长度+分隔符+字符串内容
            encoded += str(len(s)) + self.delimiter + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """将编码后的字符串解码成字符串列表

        Args:
            s: 编码后的字符串

        Returns:
            解码后的字符串列表

        解码过程中，根据分隔符和长度前缀来恢复原始字符串列表。
        """
        i = 0
        decoded = []
        while i < len(s):
            # 查找分隔符的位置，确定长度前缀
            j = s.find(self.delimiter, i)
            length = int(s[i:j])
            # 读取字符串
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded

# 测试
codec = Codec()
original_strs = ["Hello","World","你好","世界",""]  # 包括中文字符串和空字符串
encoded_str = codec.encode(original_strs)
decoded_strs = codec.decode(encoded_str)

print("原始字符串列表:", original_strs)
print("编码后的字符串:", encoded_str)
print("解码后的字符串列表:", decoded_strs)

# 核对编码和解码后的字符串列表是否相同，确保算法的正确性
assert original_strs == decoded_strs