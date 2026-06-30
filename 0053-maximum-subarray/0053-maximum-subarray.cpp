class Solution {
public:
    int maxSubArray(vector<int> nums) {
        int sum = 0;
        int max = INT_MIN;
        for(auto it : nums){
            sum = sum + it;

            if(sum > max){
                max = sum;
            }
            if(sum < 0){
                sum = 0;
            }
        }
        return max;
    }
};

