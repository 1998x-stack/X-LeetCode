#include <iostream>
#include <vector>
#include <unordered_map>
#include <cstdlib>
#include <ctime>

using namespace std;

class RandomizedSet {
public:
    vector<int> nums;
    unordered_map<int, int> valToIndex;

    RandomizedSet() {
        srand(time(nullptr)); // 初始化随机种子
    }
    
    bool insert(int val) {
        if (valToIndex.find(val) != valToIndex.end()) return false;
        nums.push_back(val);
        valToIndex[val] = nums.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        if (valToIndex.find(val) == valToIndex.end()) return false;
        int lastVal = nums.back();
        int index = valToIndex[val];
        nums[index] = lastVal;
        valToIndex[lastVal] = index;
        nums.pop_back();
        valToIndex.erase(val);
        return true;
    }
    
    int getRandom() {
        int randIndex = rand() % nums.size();
        return nums[randIndex];
    }
};

int main() {
    RandomizedSet randomizedSet;
    cout << randomizedSet.insert(1) << endl; // 返回 true
    cout << randomizedSet.remove(2) << endl; // 返回 false
    cout << randomizedSet.insert(2) << endl; // 返回 true
    cout << randomizedSet.getRandom() << endl; // 随机返回 1 或 2
    cout << randomizedSet.remove(1) << endl; // 返回 true
    cout << randomizedSet.insert(2) << endl; // 返回 false，2 已存在
    cout << randomizedSet.getRandom() << endl; // 返回 2
    return 0;
}