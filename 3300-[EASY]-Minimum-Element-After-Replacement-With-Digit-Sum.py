from math import inf


class Solution:
    """
    Intuition:
        Use modulo math to compute digit sum.

    Runtime:
        Constraints specify a maximum value of
        10^4 which means 5 digits. With n numbers,
        this gives us a runtime of O(5 * n) ~ O(n).

    Memory:
        O(1).
    """

    def minElement(self, nums: list[int]) -> int:
        res = inf

        for n in nums:
            repl = 0
            while n:
                repl += n % 10
                n //= 10

            if repl < res:
                res = repl

        return res
