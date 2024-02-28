#include <iostream>
#include <vector>
#include <utility>

// 定义一个函数，将整数转换为罗马数字
std::string intToRoman(int num) {
    // 罗马数字映射
    std::vector<std::pair<int, std::string>> roman = {
        {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
        {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
        {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
    };
    
    std::string result;
    // 遍历映射
    for (auto& [value, symbol] : roman) {
        // 计算当前符号的数量
        while (num >= value) {
            result += symbol; // 更新结果字符串
            num -= value; // 更新整数
        }
    }
    return result;
}

int main() {
    // 测试
    std::cout << intToRoman(3) << std::endl;   // 输出: III
    std::cout << intToRoman(4) << std::endl;   // 输出: IV
    std::cout << intToRoman(9) << std::endl;   // 输出: IX
    std::cout << intToRoman(58) << std::endl;  // 输出: LVIII
    std::cout << intToRoman(1994) << std::endl;// 输出: MCMXCIV
    
    return 0;
}
