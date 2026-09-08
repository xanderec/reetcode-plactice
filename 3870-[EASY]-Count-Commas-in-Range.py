class Solution:
    """
    Intuition:
        Instead of iterating from 1 to n to count commas, we can take
        a closer look at the constraints. The constraints specify that
        1 <= n <= 100,000. Notice how the upper bound 100,000 only has
        1 comma.

        Thus, our solution revolves around taking the input `n` and
        subtracting the first 999 digits that don't have commas to
        count the number of commas.

        If `n` is less than 999, then we simply return 0.

    Runtime:
        O(1).

    Memory:
        O(1).
    """

    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        return n - 999
