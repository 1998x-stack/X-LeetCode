#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word){
        for(int i = 0; i < board.size(); ++i){
            for(int j = 0; j < board[0].size(); ++j){
                if(dfs(board, word, 0, i, j)){
                    return true;
                }
            }
        }
    }
private:
    bool dfs(vector<vector<char>>& board, const string& word, int index, int x, int y) {
        if (index == word.size()) return true; // 所有字母均匹配成功
        if (x < 0 || x >= board.size() || y < 0 || y >= board[0].size()) return false; // 越界检查
        if (board[x][y] != word[index]) return false; // 字母不匹配
        
        char temp = board[x][y];
        board[x][y] = '.'; // 标记当前位置已访问
        bool found = dfs(board, word, index + 1, x + 1, y) // 向下搜索
                  || dfs(board, word, index + 1, x - 1, y) // 向上搜索
                  || dfs(board, word, index + 1, x, y + 1) // 向右搜索
                  || dfs(board, word, index + 1, x, y - 1); // 向左搜索
        board[x][y] = temp; // 回溯，恢复状态
        return found;
    }
};

int main() {
    vector<vector<char>> board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    string word = "ABCCED";
    Solution solution;
    bool result = solution.exist(board, word);
    cout << (result ? "true" : "false") << endl;
    return 0;
}