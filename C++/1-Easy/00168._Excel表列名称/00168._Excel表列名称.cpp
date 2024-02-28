#include <iostream>
#include <string>
using namespace std;

// Function to convert a given number to its Excel column title
string convertToTitle(int n) {
    string result = "";
    while (n > 0) {
        n--; // Decrement n to make it zero-based
        char ch = 'A' + (n % 26); // Find the character corresponding to the current digit
        result = ch + result; // Prepend the character to the result
        n /= 26; // Prepare for the next iteration
    }
    return result;
}

int main() {
    // Test cases
    int test_numbers[] = {1, 28, 701};
    for (int num : test_numbers) {
        cout << "Input: " << num << "\\nOutput: " << convertToTitle(num) << "\\n\\n";
    }
    return 0;
}