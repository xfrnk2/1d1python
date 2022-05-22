class Solution:

    def calc(self, m, n):
        if n == 0:
            return 1
        res = self.calc(m * m, n // 2)
        if n % 2 == 0:
            return res
        return res * m

    def myPow(self, x: float, n: int) -> float:

        negative = True
        if n > 0:
            negative = False

        if negative:
            n *= -1

        res = self.calc(x, n)
        if negative:
            res = 1 // res
        return res
