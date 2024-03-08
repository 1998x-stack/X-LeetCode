#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

// Function to find the minimum number of conference rooms required
int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;

    // Sort the meetings by their start time
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    // Use a min heap to track the end time of meetings
    priority_queue<int, vector<int>, greater<int>> minHeap;

    // Add the first meeting's end time
    minHeap.push(intervals[0][1]);

    for (int i = 1; i < intervals.size(); i++) {
        // If the current meeting can start after the earliest ended meeting
        if (intervals[i][0] >= minHeap.top()) {
            minHeap.pop(); // Room is reused
        }
        // Add the current meeting's end time
        minHeap.push(intervals[i][1]);
    }

    // The size of the heap is the number of rooms required
    return minHeap.size();
}

int main() {
    vector<vector<int>> intervals = {{0, 30}, {5, 10}, {15, 20}};
    cout << "Minimum number of meeting rooms required: " << minMeetingRooms(intervals) << endl;
    return 0;
}