class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' return sorted(s) == sorted(t) '''
        mps = {}
        mpt = {}
        for ch in s:
            mps[ch] = mps.get(ch, 0) + 1
        for ch in t:
            mpt[ch] = mpt.get(ch, 0) + 1

        return mps == mpt
        