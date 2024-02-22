def multiply(num1: str, num2: str) -> str:
    """
    实现字符串表示的两个非负整数的乘法。
    
    参数:
    num1: 非负整数的字符串表示。
    num2: 非负整数的字符串表示。
    
    返回:
    乘积的字符串表示。
    
    示例:
    >>> multiply("123", "456")
    "56088"
    
    """
    if num1 == "0" or num2 == "0":  # 边界情况：任一数为0，结果即为0
        return "0"
    
    m, n = len(num1), len(num2)
    result = [0] * (m + n)  # 初始化结果数组
    
    # 逐位相乘
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            sum = mul + result[i + j + 1]
            
            result[i + j + 1] = sum % 10  # 更新当前位
            result[i + j] += sum // 10  # 处理进位
            
    # 转换结果
    result_str = ''.join(str(x) for x in result)
    return result_str.lstrip('0')  # 去除前导零

# 示例运行
print(multiply("123", "456"))  # 应输出: "56088"