#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isNumber(string s) {
        bool numSeen = false;
        bool dotSeen = false;
        bool eSeen = false;
        int numberAfterE = true;
        
        // Trim spaces at the beginning and end
        int left = 0, right = s.size() - 1;
        while (left <= right && s[left] == ' ') ++left;
        while (left <= right && s[right] == ' ') --right;
        
        for (int i = left; i <= right; i++) {
            char c = s[i];
            
            // If it's a digit, update numSeen and numberAfterE
            if (isdigit(c)) {
                numSeen = true;
                numberAfterE = true;
            } else if (c == '.') {
                // If dot is seen or e is seen before, it's not a valid number
                if (dotSeen || eSeen) return false;
                dotSeen = true;
            } else if (c == 'e' || c == 'E') {
                // If e is seen before, or no digit before e, it's not a valid number
                if (eSeen || !numSeen) return false;
                eSeen = true;
                numberAfterE = false; // Reset for digits after e
            } else if (c == '+' || c == '-') {
                // If the sign is not at the start or after e, it's not valid
                if (i != left && s[i-1] != 'e' && s[i-1] != 'E') return false;
            } else {
                // Any other character is invalid
                return false;
            }
        }
        
        // Check if at least one digit is seen and number after e (if e is present) is valid
        return numSeen && numberAfterE;
    }
};

int main() {
    Solution solution;
    string test = "0"; // Change this string to test other inputs
    bool result = solution.isNumber(test);
    cout << (result ? "True" : "False") << endl;
    return 0;
}