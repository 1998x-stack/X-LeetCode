#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> generatePalindromes(string s) {
        unordered_map<char, int> charCount;
        for (char c : s) charCount[c]++;

        int oddCount = 0;
        string mid = "";
        string half = "";
        for (auto& p : charCount) {
            if (p.second % 2 == 1) {
                oddCount++;
                mid = p.first; // Middle character for odd length palindromes
            }
            half += string(p.second / 2, p.first); // Constructing half string
        }

        if (oddCount > 1) return {}; // Cannot form a palindrome if more than one character has odd count

        vector<string> permutations;
        sort(half.begin(), half.end()); // Sort to ensure lexicographical order for permutations
        do {
            string t = half;
            reverse(t.begin(), t.end());
            permutations.push_back(half + mid + t); // Construct the full palindrome
        } while (next_permutation(half.begin(), half.end())); // Generate all permutations of half

        return permutations;
    }
};

int main() {
    Solution solution;
    string input = "aabb";
    vector<string> palindromes = solution.generatePalindromes(input);

    for (string& palindrome : palindromes) {
        cout << palindrome << endl;
    }

    return 0;
}