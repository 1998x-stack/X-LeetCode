#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProduct(vector<string>& words) {
        int n = words.size();
        vector<int> masks(n, 0); // 用于存储每个字符串的字符掩码
        int maxProduct = 0;
        
        // 构建每个字符串的掩码
        for (int i = 0; i < n; ++i) {
            for(char c: words[i]){
                masks[i] |= 1 << (c - 'a');
            }
        }
        
        // 比较每对字符串
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if ((masks[i] & masks[j]) == 0) { // 检查是否没有共同字符
                    maxProduct = max(maxProduct, int(words[i].length() * words[j].length()));
                }
            }
        }
        
        return maxProduct;
    }
};

int main() {
    Solution solution;
    vector<string> words = {"abcw","baz","foo","bar","xtfn","abcdef"};
    cout << "Maximum product of word lengths: " << solution.maxProduct(words) << endl;
    return 0;
}