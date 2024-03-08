#include <iostream>
#include <vector>
#include <queue>
#include <list>
using namespace std;

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return {0}; // 边界情况：只有一个节点
        vector<list<int>> adj(n); // 邻接表表示图
        vector<int> degree(n, 0); // 节点的度
        for (auto& e : edges) { // 建图
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
            degree[e[0]]++;
            degree[e[1]]++;
        }
        
        queue<int> q; // 存储度数为1的节点（叶子节点）
        for (int i = 0; i < n; ++i) {
            if (degree[i] == 1) q.push(i);
        }
        
        while (n > 2) {
            int size = q.size();
            n -= size; // 删除叶子节点后，更新图中节点的数量
            for (int i = 0; i < size; ++i) {
                int t = q.front(); q.pop();
                for (auto it = adj[t].begin(); it != adj[t].end(); ++it) {
                    if (--degree[*it] == 1) q.push(*it); // 更新度数，并检查是否变成叶子节点
                }
            }
        }
        
        vector<int> result;
        while (!q.empty()) {
            result.push_back(q.front());
            q.pop();
        }
        return result;
    }
};

int main() {
    Solution solution;
    int n = 4;
    vector<vector<int>> edges = {{1, 0}, {1, 2}, {1, 3}};
    vector<int> result = solution.findMinHeightTrees(n, edges);
    for (int root : result) {
        cout << root << " ";
    }
    cout << endl;
    return 0;
}