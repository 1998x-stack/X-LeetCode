from typing import Dict, List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def clone(node: 'Node', copies: Dict[int, 'Node']) -> 'Node':
            """
            使用 DFS 递归克隆图中的每个节点及其边

            参数:
            - node: 当前正在访问的节点
            - copies: 存储已克隆节点的哈希表，键为原节点的值，值为克隆的节点实例
            
            返回:
            - 克隆的节点实例
            """
            # 如果节点为空，返回 None
            if not node:
                return None
            
            # 如果节点已经被克隆过，直接从哈希表中返回克隆的节点
            if node.val in copies:
                return copies[node.val]
            
            # 创建当前节点的克隆
            clone_node = Node(node.val)
            copies[node.val] = clone_node
            
            # 递归克隆当前节点的所有邻居，并添加到克隆节点的邻居列表中
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor, copies))
            
            return clone_node
        
        # 使用哈希表存储所有克隆的节点，以便快速访问和防止无限递归
        copies = {}
        return clone(node, copies)

# 示例代码用于测试
# 创建图的示例节点
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# 建立邻居关系
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# 克隆图
solution = Solution()
cloned_graph = solution.cloneGraph(node1)

# 检查克隆的结果（由于环境限制，此处不进行实际打印，仅示意代码运行逻辑）
# 实际使用时，可以通过遍历 cloned_graph 并打印节点及其邻居的值来验证克隆结果
