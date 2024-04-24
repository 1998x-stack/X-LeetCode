from typing import List, Dict
import os

def find_duplicate_files(paths: List[str]) -> List[List[str]]:
    """
    根据文件内容找出系统中的重复文件。

    Args:
    paths (List[str]): 文件路径和内容的列表，格式为 "root/directory file_name(content)".

    Returns:
    List[List[str]]: 包含重复文件路径的列表的列表。

    Example:
    >>> find_duplicate_files(["root/a 1.txt(abcd)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"])
    [['root/a/1.txt', 'root/c/3.txt'], ['root/c/d/4.txt']]
    """
    # 用于存储文件内容和对应文件路径的字典
    content_map: Dict[str, List[str]] = {}
    
    for path in paths:
        parts = path.split(' ')
        dir_path, files = parts[0], parts[1:]
        for file in files:
            file_name, content = file.split('(')
            content = content[:-1]
            full_path = os.path.join(dir_path, file_name)
            content_map.setdefault(content, []).append(full_path)
    
    result = [paths for paths in content_map.values() if len(paths) > 1]
    
    return result
        
# 示例运行，查看功能是否正确
test_paths = ["root/a 1.txt(abcd)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
result = find_duplicate_files(test_paths)
print(result)