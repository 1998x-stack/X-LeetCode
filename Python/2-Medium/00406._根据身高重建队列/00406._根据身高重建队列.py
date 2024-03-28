from typing import List

def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    """
    根据身高重建队列。
    
    先按身高降序、k值升序排序，然后根据k值插入到结果列表的正确位置。
    
    Args:
        people: 一个列表，包含一对整数[h, k]，h是身高，k是这个人前面比他高的人数。
    
    Returns:
        重建后的队列。
    
    Examples:
        >>> reconstruct_queue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
        [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    """
    # 按照身高降序、k值升序对people进行排序
    people.sort(key=lambda x: (-x[0], x[1]))
    
    queue = []
    for person in people:
        # 根据每个人的k值将其插入到队列的相应位置
        queue.insert(person[1], person)
    
    return queue

# 运行示例代码
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
reconstructed_queue = reconstruct_queue(people)
print(reconstructed_queue)