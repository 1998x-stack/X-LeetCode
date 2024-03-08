#include <iostream>
#include <string>
using namespace std;

// 函数用于计算公牛和奶牛的数量
string getHint(string secret, string guess) {
    int bulls = 0;
    int cows = 0;
    int numbers[10] = {0}; // 用于存储秘密数字中每个数字出现的次数

    // 第一遍扫描，找到所有的公牛
    for (int i = 0; i < secret.length(); i++) {
        if (secret[i] == guess[i]) {
            bulls++;
        } else {
            // 如果不是公牛，计数秘密数字中的数字
            numbers[secret[i] - '0']++;
        }
    }

    // 第二遍扫描，找到所有的奶牛
    for (int i = 0; i < guess.length(); i++) {
        // 只有当这个位置不是公牛，并且秘密数字中还有未被匹配的相同数字时，才算作奶牛
        if (secret[i] != guess[i] && numbers[guess[i] - '0'] > 0) {
            cows++;
            numbers[guess[i] - '0']--; // 减少该数字的剩余匹配次数
        }
    }

    return to_string(bulls) + 'A' + to_string(cows) + 'B';
}

int main() {
    string secret, guess;
    cout << "Enter secret number: ";
    cin >> secret;
    cout << "Enter guess number: ";
    cin >> guess;
    string hint = getHint(secret, guess);
    cout << "Hint: " << hint << endl;
    return 0;
}