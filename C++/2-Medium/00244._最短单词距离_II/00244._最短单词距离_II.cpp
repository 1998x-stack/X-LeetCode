#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <limits>
using namespace std;

class WordDistance {
public:
    unordered_map<string, vector<int>> wordIndices;

    WordDistance(vector<string>& words) {
        for (int i = 0; i < words.size(); ++i) {
            wordIndices[words[i]].push_back(i);
        }
    }

    int shortest(string word1, string word2) {
        vector<int>& indices1 = wordIndices[word1];
        vector<int>& indices2 = wordIndices[word2];
        int minDistance = numeric_limits<int>::max();
        int i = 0, j = 0;
        while (i < indices1.size() && j < indices2.size()) {
            minDistance = min(minDistance, abs(indices1[i] - indices2[j]));
            if (indices1[i] < indices2[j]) ++i;
            else ++j;
        }
        return minDistance;
    }
};

int main() {
    vector<string> words = {"practice", "makes", "perfect", "coding", "makes"};
    WordDistance wordDistance(words);
    cout << "Shortest distance between 'coding' and 'practice': " << wordDistance.shortest("coding", "practice") << endl;
    cout << "Shortest distance between 'makes' and 'coding': " << wordDistance.shortest("makes", "coding") << endl;
    return 0;
}