#include <iostream>
#include <vector>
#include <string>
using namespace std;

// 字符串相乘函数
string multiply(string num1, string num2) {
    if (num1 == "0" || num2 == "0") return "0";
    int m = num1.size(), n = num2.size();
    vector<int> result(m + n, 0);
    
    for (int i = m - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            int mul = (num1[i] - '0') * (num2[j] - '0');
            int sum = mul + result[i + j + 1];
            
            result[i + j + 1] = sum % 10;
            result[i + j] += sum / 10;
        }
    }
    
    string strResult;
    int i = 0;
    while (i < result.size() && result[i] == 0) ++i; // 去除结果前导零
    for (; i < result.size(); ++i) {
        strResult.push_back(result[i] + '0');
    }
    
    return strResult;
}

int main() {
    string num1 = "123", num2 = "456";
    cout << "Product of " << num1 << " and " << num2 << " is " << multiply(num1, num2) << endl;
    return 0;
}