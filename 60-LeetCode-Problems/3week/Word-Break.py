class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        d = [0 for _ in range(len(s)+1)]
        d[0] = 1
        
        for i in range(1, len(s) + 1):
            for j in range(len(wordDict)):
                wl = len(wordDict[j])
                if i - wl >= 0:
                    d[i] += (s[i-wl:i] == wordDict[j]) and d[i-wl]
        return d[-1]