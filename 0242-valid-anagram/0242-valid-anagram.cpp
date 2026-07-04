/*
class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int> mps, mpt;
        for (auto word : s){
            mps[word]++;
        }
        for (auto word : t){
            mpt[word]++;
        }
        for (auto word : s){
            if(mps[word] != mpt[word])
                return false;
        }
        for (auto word : t){
            if(mps[word] != mpt[word])
                return false;
        }
        return true;
    }
};

*/

class Solution {
public:
    bool isAnagram(string s, string t) {
map<char, int> mps, mpt;
for(auto it : s){
    mps[it]++;
}
for(auto it : t){
    mpt[it]++;
}
return mps == mpt;
    }
};