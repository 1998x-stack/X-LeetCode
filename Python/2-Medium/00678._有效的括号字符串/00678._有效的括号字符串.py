def check_valid_string(s):
    min_count = max_count = 0
    for char in s:
        if char == '(':
            min_count += 1
            max_count += 1
        elif char == ')':
            if min_count > 0:
                min_count -= 1
            max_count -= 1
        elif char == '*':
            if min_count > 0:
                min_count -= 1
            max_count += 1
        if max_count < 0:
            return False
    return min_count == 0

# 测试代码
test_cases = ["()", "(*)", "(*))", "(*()", ")*(", "*)*(", ")*"]
results = [check_valid_string(case) for case in test_cases]
print(results)  # 预期输出 [True, True, True, True, False, False, False]