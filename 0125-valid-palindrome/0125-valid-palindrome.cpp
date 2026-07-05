class Solution {
public:
    bool isPalindrome(string s) {
    string clean = "";
    for(auto it : s){
        if(isalnum(it)){
            clean += tolower(it);
        }
    }
    string rev = clean;
    reverse(rev.begin(), rev.end());
    return clean == rev;
    }
};