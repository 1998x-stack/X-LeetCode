#include <iostream>
#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head == nullptr) return NULL;

        unordered_map<Node*, Node*> copies;
        Node* current = head;
        while (current){
            copies[current] = new Node(current->val);
            current = current->next;
        }

        current = head;
        while(current){
            copies[current]->next = copies[current->next];
            copies[current]->random = copies[current->random];
        }

        return copies[head];
    }
};

int main() {
    // Example usage
    Node* node1 = new Node(7);
    Node* node2 = new Node(13);
    Node* node3 = new Node(11);
    Node* node4 = new Node(10);
    Node* node5 = new Node(1);

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;

    node2->random = node1;
    node3->random = node5;
    node4->random = node3;
    node5->random = node1;

    Solution solution;
    Node* copiedListHead = solution.copyRandomList(node1);

    // Printing the copied list to verify the solution
    Node* current = copiedListHead;
    while (current) {
        cout << "Value: " << current->val << ", Random Value: ";
        if (current->random) {
            cout << current->random->val;
        } else {
            cout << "null";
        }
        cout << endl;
        current = current->next;
    }

    // Cleaning up the allocated nodes (in a real scenario, consider smart pointers to manage memory automatically)
    delete node1;
    delete node2;
    delete node3;
    delete node4;
    delete node5;
    
    // Also, delete the copied nodes
    while (copiedListHead) {
        Node* temp = copiedListHead;
        copiedListHead = copiedListHead->next;
        delete temp;
    }

    return 0;
}