from typing import List, Dict
from collections import defaultdict

class Solution:
    def __init__(self):
        # 初始化并查集
        self.parent = {}
        
    def find(self, x: str)->str:
        # 查找根节点，并进行路径压缩
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        # 初始化并查集
        for account in accounts:
            name = account[0]
            for email in accounts[1:]:
                if email not in self.parent:
                    self.parent[email] = email
                email_to_name[email] = name
                self.union(account[1], email)
        
        email_grouped_by_root = defaultdict(list)
        for email in self.parent:
            root = self.find(email)
            email_grouped_by_root[root].append(email)
        
        # 收集并排序每组的邮箱，生成最终结果
        merged_accounts = []
        for emails in email_grouped_by_root.values():
            name = email_to_name[emails[0]]
            merged_accounts.append([name] + sorted(emails))
        
        return merged_accounts
    

# 创建示例输入
accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]

# 实例化解决方案并运行
sol = Solution()
merged_accounts = sol.accountsMerge(accounts)
print(merged_accounts)