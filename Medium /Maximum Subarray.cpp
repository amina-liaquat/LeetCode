#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = INT_MIN;
        int currSum = 0;

        // Kadane's Algorithm - O(n)
        for (int i = 0; i < nums.size(); i++) {
            currSum += nums[i];
            maxSum = max(maxSum, currSum);
            
            if (currSum < 0) {
                currSum = 0;
            }
        }
        
        return maxSum;
    }
};
