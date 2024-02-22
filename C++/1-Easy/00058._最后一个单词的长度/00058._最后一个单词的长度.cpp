#include <iostream>
#include <string>
using namespace std;

int lengthOfLastWord(string s) {
    int length = 0; // 初始化计数器为0
    int index = s.size() - 1; // 从字符串的最后一个字符开始

    // 跳过末尾的空格
    while (index >= 0 && s[index] == ' ') index--;

    // 计算最后一个单词的长度
    while (index >= 0 && s[index] != ' ') {
        length++;
        index--;
    }

    return length;
}

int main() {
    string s = "Hello World";
    cout << "Length of last word: " << lengthOfLastWord(s) << endl;
    return 0;
}