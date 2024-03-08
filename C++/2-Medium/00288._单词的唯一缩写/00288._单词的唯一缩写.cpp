#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class ValidWordAbbr {
public:
    unordered_map<string, unordered_set<string>> abbrDict;

    // Helper function to generate abbreviation of a word
    string generateAbbr(const string& word) {
        int n = word.length();
        if (n <= 2) return word;
        return word.front() + to_string(n - 2) + word.back();
    }

    ValidWordAbbr(vector<string>& dictionary) {
        for (string& word : dictionary) {
            abbrDict[generateAbbr(word)].insert(word);
        }
    }

    // Check if the abbreviation of a word is unique in the dictionary
    bool isUnique(string word) {
        string abbr = generateAbbr(word);
        if (abbrDict.find(abbr) == abbrDict.end()) return true;
        else if (abbrDict[abbr].size() == 1 && abbrDict[abbr].count(word)) return true;
        return false;
    }
};

int main() {
    // Example usage
    vector<string> dictionary = {"deer", "door", "cake", "card"};
    ValidWordAbbr vwa(dictionary);
    cout << (vwa.isUnique("dear") ? "True" : "False") << endl;
    cout << (vwa.isUnique("cart") ? "True" : "False") << endl;
    cout << (vwa.isUnique("cane") ? "True" : "False") << endl;
    cout << (vwa.isUnique("make") ? "True" : "False") << endl;
    return 0;
}