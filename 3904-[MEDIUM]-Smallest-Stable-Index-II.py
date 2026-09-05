from math import inf


class Solution:
    """
    Intuition:
        The problem statement for the II variant is the same as the base I
        variant. The intuition is also largely the same.

        The difference is that we reduce the need for 3 linear scans to 2
        by scanning from right to left first to find the smallest elmt on
        the right partition of each index.

        Then, we can scan left to right to accumulate the largest elmt. In
        this loop, as soon as we hit an index for which the curr max minus
        the right side min is less than or eq to k, we have found our soln.

    Runtime:
        O(n) for 2 linear scans.

    Memory:
        O(n) to store the right partition min values for each index.
    """

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)
        inst = [0] * N

        small = inf
        for i in range(N - 1, -1, -1):
            if nums[i] < small:
                small = nums[i]

            inst[i] = small

        large = 0
        for i in range(N):
            if nums[i] > large:
                large = nums[i]

            if large - inst[i] <= k:
                return i

        return -1
