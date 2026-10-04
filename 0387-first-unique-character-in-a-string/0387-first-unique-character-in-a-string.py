class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

        for k,v in freq.items():
            if v == 1:
                return s.index(k)
            
        return -1
        