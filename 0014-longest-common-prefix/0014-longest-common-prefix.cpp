class Solution {
public:
    string longestCommonPrefix(vector<string>& s) {
        sort(s.begin(), s.end());
        string first = s.front();
        string last = s.back();
        string word = "";
        
        for(int i = 0; i < min(first.size(), last.size()); i++){
            if(first[i] == last[i]){
                word = word + first[i];
            }else{
                break;
            }
        }
        return word;
    }
};