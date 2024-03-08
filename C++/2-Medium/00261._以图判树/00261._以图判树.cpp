#include <iostream>
#include <vector>
using namespace std;

class UnionFind {
public:
    vector<int> parent;
    UnionFind(int size) {
        parent.resize(size);
        for (int i = 0; i < size; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]); // 路径压缩
        }
        return parent[x];
    }

    bool unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY) {
            return false; // 发现环
        }
        parent[rootX] = rootY; // 合并
        return true;
    }
};

bool validTree(int n, vector<vector<int>>& edges) {
    if (edges.size() != n - 1) return false; // 边的数量不是 n-1，直接返回 false
    UnionFind uf(n);
    for (auto& edge : edges) {
        if (!uf.unionSet(edge[0], edge[1])) {
            return false; // 如果合并失败，说明存在环
        }
    }
    return true;
}

int main() {
    // 示例 1
    vector<vector<int>> edges1 = {{0,1}, {0,2}, {0,3}, {1,4}};
    cout << "Example 1: " << (validTree(5, edges1) ? "true" : "false") << endl;
    
    // 示例 2
    vector<vector<int>> edges2 = {{0,1}, {1,2}, {2,3}, {1,3}, {1,4}};
    cout << "Example 2: " << (validTree(5, edges2) ? "true" : "false") << endl;
    
    return 0;
}