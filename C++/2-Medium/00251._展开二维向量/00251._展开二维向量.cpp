#include <iostream>
#include <vector>
using namespace std;

class Vector2D {
private:
    vector<vector<int>> vec;
    int row, col;

public:
    Vector2D(vector<vector<int>>& v) {
        vec = v;
        row = 0;
        col = 0;
    }

    int next() {
        // Move to the next element if the current one is not valid
        if (!hasNext()) return -1; // Just for safety, normally hasNext should be called before next
        return vec[row][col++];
    }

    bool hasNext() {
        // Skip empty rows
        while (row < vec.size() && col == vec[row].size()) {
            row++;
            col = 0;
        }
        // Check if there is any element left
        return row < vec.size();
    }
};

int main() {
    vector<vector<int>> v = {{1, 2}, {3}, {4, 5, 6}};
    Vector2D iterator(v);
    
    while (iterator.hasNext()) cout << iterator.next() << " ";
    
    return 0;
}