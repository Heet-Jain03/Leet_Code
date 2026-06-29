class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        long long rev = 0;
        long long ori = x;
        while(x != 0){
            long long num = x % 10;
            x = x / 10;
            rev = (rev * 10) + num; 
        }
        if (rev == ori){
            return true;
        }
        return false;
    }
};