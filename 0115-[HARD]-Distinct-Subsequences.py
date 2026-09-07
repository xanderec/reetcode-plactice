class Solution1:
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


class Solution2:
    """
    Intuition:
        Bottom-up tabulation approach. Turns our heavy recursive soln
        into a fast iterative soln.

        Let the function F(i, j) output the number of distinct subseqs
        equal to t[:j] we can form using prefix s[:i]. To solve for that,
        we need to consider how many distinct subseqs we can form using
        s[:i - 1] i.e. F(i - 1, j). If s[i] == t[j], then we also have
        to consider how many distinct subseqs equal to t[:j - 1] we can
        form using s[:i - 1].

        Thus, the recurrence relation becomes:

            F(i, j) = F(i - 1, j) if s[i] != t[j]

            F(i, j) = F(i - 1, j) + F(i - 1, j - 1) if s[i] == t[j].

        Notice how the recurrence relation only depends on state i - 1 at
        state i. Since we only ever depend on the previous row, we can
        collapse the need for a 2D cache to 1D. The cache simply represents
        the current row of state.

    Runtime:
        Still O(m * n).

    Memory:
        O(n) for the cache.
    """

    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        # early exit
        if N > M:
            return 0

        # base case at ix=0, only 1 way to form empty str i.e. len 0
        #
        # dp table answers: how many distinct subseqs equal to t[:j]
        # can we form using prefix s[:i]
        dp = [1] + [0] * N

        for i in range(1, M + 1):
            # call to min() is to cap when i is small, we haven't
            # explored N chars yet in s
            #
            # we iterate backwards to prevent double counting when
            # transitioning to next row of state
            for j in range(min(i, N), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[N]
