def repeated_string_match(A, B):
    repeated = A
    repeated_count = 1
    while len(repeated) < len(B):
        repeated += A
        repeated_count += 1
    if B in repeated:
        return repeated_count
    if B in repeated + A:
        return repeated_count + 1
    return -1

print(repeated_string_match("abcd", "cdabcdab"))  # 3