#include <iostream>
using namespace std;

// Function to calculate the square root of x
int sqrt(int x) {
    if (x == 0 || x == 1) return x;
    long long left = 1, right = x, ans = 0;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if (mid * mid == x) return mid;
        if (mid * mid < x) {
            left = mid + 1;
            ans = mid; // Update ans to the last mid value
        } else {
            right = mid - 1;
        }
    }
    return ans;
}

int main() {
    int x;
    cout << "Enter a non-negative integer: ";
    cin >> x;
    cout << "The square root of " << x << " is " << sqrt(x) << endl;
    return 0;
}