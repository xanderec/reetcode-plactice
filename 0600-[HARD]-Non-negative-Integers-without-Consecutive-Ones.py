class Solution:
    """
    Intuition:
        Binary digit DP problem. We memoize using top down approach
        by constructing the binary string of our upper bound and
        choosing bits at each position.

        We prune states leading to consecutive 1 bits.

    Runtime:
        Total runtime is (num of possible states) * (work per state).

        We have 2 possible values for tight, 2 possible values for
        the previous bit, and log n bits for an integer n. This means
        we have 2 * 2 * log n ~ log n possible states.

        For each state, we iterate through up to 2 values (the next
        bit we choose), so constant time.

        Overall, this yields a runtime complexity of O(log n).

    Memory:
        We have log n different states (computed previously) which
        means O(log n) space for the memo cache.

        Our recursion tree's depth is at most the number of digits
        i.e. O(log n) once more.

        Total memory complexity is thus O(log n) as well.
    """

    def findIntegers(self, n: int) -> int:
        bits = [int(digit) for digit in bin(n)[2:]]
        N = len(bits)
        # track position, previous bit, tightness -- init w -1 sentinels
        memo = [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(N)]

        def dp(pos, prevBit, tight):
            # finished choosing bits
            if pos == N:
                return 1

            # fetch from memo cache
            if memo[pos][prevBit][tight] != -1:
                return memo[pos][prevBit][tight]

            limit = bits[pos] if tight else 1
            res = 0
            for b in range(limit + 1):
                # skip consecutive 1's
                if b == 1 and prevBit == 1:
                    continue

                # compute res
                res += dp(pos + 1, b, 1 if tight and b == bits[pos] else 0)

            # populate cache & return res
            memo[pos][prevBit][tight] = res
            return res

        return dp(0, 0, 1)
