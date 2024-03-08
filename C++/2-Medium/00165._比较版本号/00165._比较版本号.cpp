#include <iostream>
#include <vector>
#include <string>
using namespace std;

// 分割字符串函数，以 '.' 为分隔符
vector<int> splitVersion(const string& version) {
    vector<int> nums;
    int start = 0;
    for(int i=0; i <= version.size(); ++i){
        if(i==version.size() || version[i] == '.'){
            nums.push_back(stoi(version.substr(start, i-start)));
            start = i + 1;
        }
    }
    return nums;
}

// 比较版本号
int compareVersion(string version1, string version2) {
    vector<int> nums1 = splitVersion(version1), nums2 = splitVersion(version2);
    int n1 = nums1.size(), n2 = nums2.size();
    
    // 比较每个修订号
    for (int i = 0; i < max(n1, n2); ++i) {
        // 获取当前位置的修订号，如果超出版本号长度，则为0
        int v1 = i < n1 ? nums1[i] : 0;
        int v2 = i < n2 ? nums2[i] : 0;
        if (v1 < v2) return -1;
        else if (v1 > v2) return 1;
    }
    return 0; // 所有修订号都相等
}

int main() {
    // 示例测试
    cout << compareVersion("1.01", "1.001") << endl; // 应输出 0
    cout << compareVersion("1.0", "1.0.0") << endl;  // 应输出 0
    cout << compareVersion("0.1", "1.1") << endl;    // 应输出 -1
    return 0;
}