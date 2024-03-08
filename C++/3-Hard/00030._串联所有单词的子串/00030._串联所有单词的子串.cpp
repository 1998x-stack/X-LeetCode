#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

vector<int> findSubstring(string s, vector<string>& words) {
    vector<int> indices;
    if(s.empty() || words.empty()) return indices;

    int wordLength = words[0].size();
    int wordCount = words.size();
    int substringLength = wordLength * wordCount;

    unordered_map<string, int> wordCountMap;
    for(const auto& word : words){
        ++wordCountMap[word];
    }

    for(int i = 0; i <= static_cast<int>(s.length()) - substringLength; ++i){
        unordered_map<string, int> seenWords;
        int j = 0;
        for(; j < wordCount; ++j){
            string word = s.substr(i + j * wordLength, wordLength);
            if(wordCountMap.find(word) == wordCountMap.end()){
                break;
            }
            ++seenWords[word];
            if(seenWords[word] > wordCountMap[word]){
                break;
            }
        }
        if(j == wordCount){
            indices.push_back(i);
    }
    return indices;
}

int main() {
    string s = "barfoothefoobarman";
    vector<string> words = {"foo", "bar"};
    vector<int> indices = findSubstring(s, words);

    cout << "Indices: ";
    for (int index : indices) {
        cout << index << " ";
    }
    cout << endl;

    return 0;
}