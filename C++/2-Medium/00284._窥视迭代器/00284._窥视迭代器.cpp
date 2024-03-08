#include <vector>
#include <iostream>
using namespace std;

class Iterator {
    struct Data;
    vector<int> nums;
    int index = 0;
public:
    Iterator(const vector<int>& nums) : nums(nums) {}
    Iterator(const Iterator& iter) : nums(iter.nums) {}
    virtual ~Iterator() {}
    // Returns the next element in the iteration.
    int next() {
        return nums[index++];
    }
    // Returns true if the iteration has more elements.
    bool hasNext() const {
        return index < nums.size();
    }
};

class PeekingIterator : public Iterator {
private:
    bool hasPeeked;
    int nextElement;
public:
    PeekingIterator(const vector<int>& nums) : Iterator(nums), hasPeeked(false), nextElement(0) {}

    int peek() {
        if (!hasPeeked) {
            if (Iterator::hasNext()) {
                nextElement = Iterator::next();
                hasPeeked = true;
            }
        }
        return nextElement;
    }

    int next() {
        if (!hasPeeked) {
            return Iterator::next();
        }
        int returnValue = nextElement;
        hasPeeked = false;
        return returnValue;
    }

    bool hasNext() const {
        return hasPeeked || Iterator::hasNext();
    }
};

int main() {
    vector<int> nums = {1, 2, 3};
    PeekingIterator it(nums);
    
    cout << it.peek() << endl;  // Should return 1
    cout << it.next() << endl;  // Should return 1
    cout << it.peek() << endl;  // Should return 2
    cout << it.next() << endl;  // Should return 2
    cout << it.next() << endl;  // Should return 3
    cout << (it.hasNext() ? "true" : "false") << endl;  // Should return false
    return 0;
}