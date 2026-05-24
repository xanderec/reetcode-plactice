from math import inf


class Solution:
    """
    Intuition:
        We use a top-down DP approach and store the current position
        as the only piece of state.

        We start each recursive step by computing all the neighbours
        in the interval [pos - d, pos + d] that we can jump to. Our
        base case here is when we can't jump to any other neighbour,
        in which case we know the answer is 1. Otherwise, we iterate
        through all possible jumps and compute the maximum.

        We also start the DP search from every index to find the one
        yiedling the max amt of jumps.

    Runtime:
        We have n possible positions or states. At each state, we
        incur up to O(d) amount of work, which leads our runtime
        complexity to be bounded by O(n * d).

    Memory:
        O(n) for the memo cache.

        O(n) for the recursive stack depth.

        Overall, O(n) memory.
    """

    def maxJumps(self, arr: list[int], d: int) -> int:
        # need dest to be smaller than curr
        N = len(arr)
        memo = [-inf] * N

        def dp(pos):
            # scan neighbours
            canJump = []
            curr = arr[pos]
            l, r = max(0, pos - d), min(N - 1, pos + d)
            # go left
            for j in range(pos - 1, l - 1, -1):
                if arr[j] >= curr:
                    break

                if arr[j] < curr:
                    canJump.append(j)
            # go right
            for j in range(pos + 1, r + 1):
                if arr[j] >= curr:
                    break

                if arr[j] < curr:
                    canJump.append(j)

            # base case -- nowhere to go
            if not canJump:
                memo[pos] = 1

            for nextPos in canJump:
                # fetch from memo if initialized
                if memo[nextPos] != -inf:
                    memo[pos] = max(memo[pos], 1 + memo[nextPos])
                # transition state
                else:
                    res = dp(nextPos)
                    memo[pos] = max(memo[pos], 1 + res)

            return memo[pos]

        res = 0
        for i in range(N):
            res = max(res, dp(i))

        return res
