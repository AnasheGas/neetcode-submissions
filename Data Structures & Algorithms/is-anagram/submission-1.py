class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        Stable, Ttable = {}, {}

        for i in range(len(s)):
            Ttable[t[i]] = 1 + Ttable.get(t[i], 0)
            Stable[s[i]] = 1 + Stable.get(s[i], 0)
        
        if Stable != Ttable:
            return False
        
        return True


        