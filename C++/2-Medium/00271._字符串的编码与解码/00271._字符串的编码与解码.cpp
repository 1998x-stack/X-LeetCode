#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        ostringstream out;
        for (const string& str : strs) {
            out << str.size() << '|' << str;
        }
        return out.str();
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> strs;
        int i = 0;
        while (i < s.size()) {
            int j = s.find('|', i);
            int len = stoi(s.substr(i, j - i));
            strs.push_back(s.substr(j + 1, len));
            i = j + 1 + len;
        }
        return strs;
    }
};

int main() {
    Codec codec;
    vector<string> strs = {"Hello", "World"};
    string encoded = codec.encode(strs);
    vector<string> decoded = codec.decode(encoded);
    
    cout << "Encoded: " << encoded << endl;
    cout << "Decoded: ";
    for (const string& str : decoded) {
        cout << str << " ";
    }
    cout << endl;
    
    return 0;
}