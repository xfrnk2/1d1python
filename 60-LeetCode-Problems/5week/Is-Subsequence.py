
class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        m = 0
        for c in s:
            r = t.find(c, m, len(t))
            if r == -1:
                return False
            m = r+1
        return True
            