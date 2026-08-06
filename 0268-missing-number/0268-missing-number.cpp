class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int ori = 0;
        int exp = n*(n+1) / 2;
        for(auto it : nums){
            ori = ori + it;
        }
        return exp - ori;
    }
};