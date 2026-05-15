class Solution:
    """
    Intuition:
        Initially thought of using a 2 ptr approach; one ptr traversing the string
        and the other ptr travesing the pattern. However, the '*' wildcard matches
        on zero or more occurrences, meaning we can branch to multiple next states.
        2 ptrs only support tracking 1 state, so we cannot keep track of all the
        branching. The only other viable option would be DP.

        We use a top-down memo + recursive DP soln. Our memo cache dp[i][j] tracks
        if s[i:] matches p[j:]. The base case of recursive helper is when we consume
        the entire pattern and have to check if we have also consumed the entire
        string. Then, our state transitions are defined by the 2 cases of "atomic"
        chunks we encounter in the pattern. If we encounter any char or '.', then
        we simply check for a match and consume a position in the string and pattern.
        The second case is when we have a char chained with '*'. In that case, we
        can consume no chars in the string 's' or check for a match on the char in 's'
        and consume it.

    Runtime:
        Let n be the len of s and m be the len of p.

        We have n * m possible states. At each state, we transition to at most 2
        subproblems, which equates to constant time cost. Thus, the overall time
        complexity is O(m * n) i.e. number of possible states multiplied by work
        at each state.

    Memory:
        Let n be the len of s and m be the len of p.

        O(n * m) memory to store all possible states in memo cache.
    """

    def isMatch(self, s: str, p: str) -> bool:
        N, M = len(s), len(p)
        # dp[i][j] = does s[i:] match p[j:] -- init w/ sentinels
        memo = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]

        # i = pos in s, j = pos in p
        def dp(i, j):
            # base case -- when exhausted pattern, check that string has been fully consumed
            if j == M:
                return i == N

            # serve from cache
            if memo[i][j] != -1:
                return memo[i][j]

            # "atomic" pieces of pattern p:
            # - char or '.' both match exactly one char
            # - char chained with '*' matches zero or more

            # guard on i < N to prevent reading index out of bounds on s
            match = i < N and (p[j] == "." or s[i] == p[j])

            # case char chained w/ '*'
            if j < M - 1 and p[j + 1] == "*":
                memo[i][j] = dp(i, j + 2) or (match and dp(i + 1, j))
            # case char or '.'
            else:
                memo[i][j] = match and dp(i + 1, j + 1)

            return memo[i][j]

        dp(0, 0)
        return memo[0][0]
