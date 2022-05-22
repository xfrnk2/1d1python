class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        d = dict()

        for c in s:
            d[c] = d.get(c, 0) + 1
        print(d)
        for idx, c in enumerate(s):
            if d[c] < 2:
                ans = idx
                break

        return ans
