from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr: List[int] = []
        self.cal(arr, "", 0, 0, n)
        return arr

    def cal(self, arr, cur, opened, closed, n):
        if len(cur) == n * 2:
            arr.append(cur)
            return

        if opened < n:
            self.cal(arr, cur + "(", opened + 1, closed, n)
        if opened > closed:
            self.cal(arr, cur + ")", opened, closed + 1, n)
