#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution{
public:
    vector<string> restoreIpAddresses(string s){
        vector<string> result;
        vector<string> ip;
        backtrack(s, 0, ip, result);
        return result;
    }

    void backtrack(string s, int start, vector<string>& ip, vector<string>& result){
        // 如果已经得到了四段ip地址并且start已经到了s的末尾
        if(ip.size() == 4 && start == s.size()){
            result.push_back(ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + ip[3]);
            return;
        }

        if(ip.size() == 4 || start == s.size()){
            return;
        }

        for(int len = 1; len <= 3; len++){
            if(start + len > s.size()){
                break;
            }

            string segment = s.substr(start, len);
            if(segment.size() > 1 && segment[0] == '0'){
                break;
            }
            if(stoi(segment) > 255){
                break;
            }
            ip.push_back(segment);
            backtrack(s, start + len, ip, result);
            ip.pop_back();
        }
    }
};

int main() {
    Solution solution;
    string s = "25525511135";
    vector<string> result = solution.restoreIpAddresses(s);
    for(string ip : result) {
        cout << ip << endl;
    }
    return 0;
}