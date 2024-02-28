
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Node{
    public:
    int val;
    vector<Node*> neighbors;

    Node(){
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val){
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors){
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
    public:
    unordered_map<Node*, Node*> clonedNodes;

    Node* cloneGraph(Node* node){
        if(node == nullptr){
            return nullptr;
        }

        if(clonedNodes.find(node) != clonedNodes.end()){
            return clonedNodes[node];
        }

        Node* clone = new Node(node->val);
        clonedNodes[node] = clone;
        for(Node* neighbor : node->neighbors){
            clone->neighbors.push_back(cloneGraph(neighbor));
        }

        return clone;
    }
};

int main() {
    // 示例：创建一个简单的图 (1 -- 2 -- 3 -- 4 -- 1)
    Node* node1 = new Node(1);
    Node* node2 = new Node(2);
    Node* node3 = new Node(3);
    Node* node4 = new Node(4);
    node1->neighbors = {node2, node4};
    node2->neighbors = {node1, node3};
    node3->neighbors = {node2, node4};
    node4->neighbors = {node1, node3};

    Solution solution;
    Node* clonedGraph = solution.cloneGraph(node1);

    // 输出克隆图的验证信息（此处简化，实际需要遍历图来验证）
    cout << "Cloned graph's node 1 value: " << clonedGraph->val << endl;

    return 0;
}