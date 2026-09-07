class Solution:
    """
    Intuition:
        Use a top-down memoization approach.

        Our base cases rely on when we have either exhausted the
        input string s or we have found a match.

        We try to serve from cache if we can.

        If that's not possible, we count the case where we skip
        the current char in s OR we include it. Note that we can
        only count including curr char in s if we have a match.

    Runtime:
        Let m be the len of s and n be the len of t.

        We have m * n possible states, so runtime will be O(m * n).

    Memory:
        We have a max recursion depth of m since we only stop
        searching once we have fully consumed s.

        The memo table takes up O(m * n) space.

        Overall, O(m * n + m) ~ O(m * n) space.
    """

    def numDistinct(self, s: str, t: str) -> int:
        # -1 = uninitialized
        cache = [[-1] * len(s) for _ in range(len(t))]

        def dp(sx, tx):
            # found a match
            if tx == len(t):
                return 1

            # consumed whole string s
            if sx == len(s):
                return 0

            # lookup in cache
            if cache[tx][sx] != -1:
                return cache[tx][sx]

            res = dp(sx + 1, tx)  # skip curr pos in s
            if s[sx] == t[tx]:
                # include curr pos in s
                res += dp(sx + 1, tx + 1)

            cache[tx][sx] = res
            return cache[tx][sx]

        dp(0, 0)
        return cache[0][0]
