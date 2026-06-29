// hash[s[r]] -> s = "abc", r = 0 , s[r] = 'a', hash['a'], hash[97], hash[97] = 0 

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    int n = s.size();
    int l=0;
    int r=0;
    vector<int> hash(256,-1);
    int maxLength=0;

    while(r<n){
        if(hash[s[r]] != -1){ // Have I seen this character before?
            if(hash[s[r]] >= l){ // Is that old occurrence inside my current substring?
               l =  hash[s[r]] + 1; // Yes? Move the left boundary to remove the duplicate.
            }
        }
        int length = r - l + 1; //Find the size of the current valid substring.
        maxLength = max(maxLength,length);
        hash[s[r]] = r; // 0, 1, 2 index
        r++;
    }
    return maxLength; 
}
};





