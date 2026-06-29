class Solution {
public:
    string longestCommonPrefix(vector<string> str) {

    sort(str.begin(), str.end());
    string first = str.front();
    string last = str.back();
    string word = "";

    for(int i = 0; i < min(first.size(), last.size()); i++){
        if(first[i] == last[i]){
            word = word + first[i];
        }else{
            break;
        }}
        
    return word;
    }
};

