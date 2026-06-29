class Solution {
public:
    int reverse(int x) {
        long long rev = 0;
        while(x != 0) {
        long long num = x % 10; // Take the last digit
        x = x / 10; // Remove the last digit
        rev = (rev * 10) + num; // Attach that digit
        }
        if (rev > INT_MAX || rev < INT_MIN){ 
            return 0;
        }
    return (int)rev;
}
};


