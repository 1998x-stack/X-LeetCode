#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> currentPartition;
        dfs(0, s, currentPartition, result);
        return result;
    }
private:
    void dfs(int start, const string &s, vector<string> &currentPartition, vector<vector<string>> &result){
        if(start >= s.size()){
            result.push_back(currentPartition);
            return;
        }

        for(int end = start; end < s.size(); ++end){
            if(isPalindrome(s, start, end)){
                currentPartition.push_back(s.substr(start, end-start+1));
                dfs(end + 1, s, currentPartition, result);
                currentPartition.pop_back();
            }
        }
    }
    bool isPalindrome(const string &s, int start, int end){
        while(start < end){
            if(s[start++] != s[end--]){
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution solution;
    string s = "aab";
    vector<vector<string>> result = solution.partition(s);

    for (const auto &partition : result) {
        for (const string &p : partition) {
            cout << p << " ";
        }
        cout << endl;
    }

    return 0;
}