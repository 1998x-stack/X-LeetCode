#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        int n = prices.size();
        vector<int> hold(n, 0), notHold(n, 0), notHold_cooldown(n, 0);
        
        hold[0] = -prices[0];
        notHold[0] = 0;
        notHold_cooldown[0] = 0;
        
        for (int i = 1; i < n; ++i) {
            hold[i] = max(hold[i - 1], notHold[i - 1] - prices[i]);
            notHold_cooldown[i] = hold[i - 1] + prices[i];
            notHold[i] = max(notHold[i - 1], notHold_cooldown[i - 1]);
        }
        
        return max(notHold[n - 1], notHold_cooldown[n - 1]);
    }
};

int main() {
    vector<int> prices = {1, 2, 3, 0, 2};
    Solution sol;
    cout << "Max profit: " << sol.maxProfit(prices) << endl;
    return 0;
}