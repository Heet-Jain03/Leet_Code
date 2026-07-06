class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int low = INT_MAX;
        int high = INT_MIN;
        for(auto it : prices){
            int sell = it;
            low = min(low, it);
            int buy = sell - low;
            high = max(high, buy);
        }
        return high;
    }
};
