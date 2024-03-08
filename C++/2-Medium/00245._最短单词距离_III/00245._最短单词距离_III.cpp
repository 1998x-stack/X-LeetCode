#include <iostream>
#include <vector>
#include <string>
#include <climits>
using namespace std;

int shortestWordDistance(vector<string>& wordsDict, string word1, string word2) {
    int index1 = -1, index2 = -1, minDistance = INT_MAX;
    bool sameWord = word1 == word2;
    for (int i = 0; i < wordsDict.size(); ++i) {
        if (wordsDict[i] == word1) {
            if (sameWord && index1 != -1) {
                // 对于相同的单词，更新最短距离并将当前位置赋给index2
                minDistance = min(minDistance, i - index1);
                index2 = index1;
            }
            index1 = i;
        } else if (wordsDict[i] == word2) {
            index2 = i;
        }
        if (index1 != -1 && index2 != -1 && !sameWord) {
            // 对于不同的单词，计算并更新最短距离
            minDistance = min(minDistance, abs(index1 - index2));
        }
    }
    return minDistance;
}

int main() {
    vector<string> wordsDict = {"practice", "makes", "perfect", "coding", "makes"};
    string word1 = "makes";
    string word2 = "coding";
    cout << "Minimum distance: " << shortestWordDistance(wordsDict, word1, word2) << endl;

    word1 = "makes";
    word2 = "makes";
    cout << "Minimum distance: " << shortestWordDistance(wordsDict, word1, word2) << endl;
    return 0;
}