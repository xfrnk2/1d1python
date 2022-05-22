class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        t = []
        for c in s:
            if c in '({[':
                t.append(c)
            elif c in ')}]':
                if not t:
                    return False
                o = t.pop()
                if d[c] != o:
                    return False
        return len(t) == 0
