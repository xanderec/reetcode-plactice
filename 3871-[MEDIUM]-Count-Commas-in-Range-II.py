class Solution:
    """
    Intuition:
        Our intuition revolves around the following series of
        observations:

        Each number in range [1, 1000) has 0 commas.

        Each number in range [1000, 1 000 000) has 1 comma.

        Each number in range [1 000 000, 1 000 000 000) has 2 commas.

        Etc.

        We notice that for each increase in order of magnitude by
        1000, we increase the number of commas by 1. As such, we can
        reason about the problem by counting the numbers with at
        least 1 comma, then the numbers with at least 2 commas, etc.

    Runtime:
        Every iteration of the loop, we increase the comma threshold
        `sub` by a magnitude of 1000. Thus, we have a runtime of
        O(log_1000(n)) ~ O(log n).

    Memory:
        O(1).
    """

    def countCommas(self, n: int) -> int:
        res = 0
        sub = 999

        while n - sub > 0:
            res += n - sub
            sub = sub * 1000 + 999

        return res
