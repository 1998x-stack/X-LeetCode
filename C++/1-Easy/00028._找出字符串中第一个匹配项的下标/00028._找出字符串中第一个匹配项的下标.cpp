#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Function to create the LPS (Longest Prefix Suffix) array
vector<int> computeLPSArray(const string& needle) {
    int length = 0; // length of the previous longest prefix suffix
    int i = 1;
    vector<int> lps(needle.size(), 0);

    // the loop calculates lps[i] for i = 1 to M-1
    while (i < needle.size()) {
        if (needle[i] == needle[length]) {
            length++;
            lps[i] = length;
            i++;
        } else { // (needle[i] != needle[length])
            if (length != 0) {
                length = lps[length - 1];
                // Note that we do not increment i here
            } else { // if (length == 0)
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

// KMP algorithm to find the first occurrence of the needle in the haystack
int strStr(string haystack, string needle) {
    if (needle.empty()) return 0;
    vector<int> lps = computeLPSArray(needle);

    int i = 0; // index for haystack
    int j = 0; // index for needle
    while (i < haystack.size()) {
        if (needle[j] == haystack[i]) {
            i++;
            j++;
        }
        if (j == needle.size()) {
            return i - j; // found the match
        }

        // mismatch after j matches
        else if (i < haystack.size() && needle[j] != haystack[i]) {
            // Do not match lps[0..lps[j-1]] characters,
            // they will match anyway
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i = i + 1;
            }
        }
    }
    return -1; // did not find the match
}

int main() {
    string haystack = "sadbutsad";
    string needle = "sad";
    cout << "Index of first occurrence: " << strStr(haystack, needle) << endl;
    return 0;
}