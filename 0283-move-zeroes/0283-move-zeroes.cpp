class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int a = 0;
        int b = 0;
        int n = nums.size();
        while(a < n){
            if(nums[a] != 0){
                swap(nums[a], nums[b]);
                b++;
            }
            a++;
        }
    }
};