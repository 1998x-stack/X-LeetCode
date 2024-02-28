#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

// Function to simplify the given Unix-style path
string simplifyPath(string path) {
    vector<string> stack;
    stringstream ss(path);
    string curr;
    
    while (getline(ss, curr, '/')) {
        if (curr == "" || curr == ".") continue;
        if (curr == ".." && !stack.empty()) stack.pop_back();
        else if (curr != "..") stack.push_back(curr);
    }
    
    string simplifiedPath = "";
    for (auto &dir : stack) {
        simplifiedPath += "/" + dir;
    }
    
    return simplifiedPath.empty() ? "/" : simplifiedPath;
}

int main() {
    // Test cases
    cout << simplifyPath("/home/") << endl;  // Output: /home
    cout << simplifyPath("/../") << endl;    // Output: /
    cout << simplifyPath("/home//foo/") << endl;  // Output: /home/foo
    cout << simplifyPath("/a/./b/../../c/") << endl;  // Output: /c
    
    return 0;
}