from math import inf


class Solution:
    """
    Intuition:
        Brute force approach.

    Runtime:
        O(n^3) since 3 loops.

    Memory:
        O(1).
    """

    def minimumDistance(self, nums: list[int]) -> int:
        # early return for base case
        if len(nums) < 3:
            return -1

        res = inf
        N = len(nums)

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if nums[i] == nums[j] == nums[k]:
                        res = min(res, abs(i - j) + abs(j - k) + abs(k - i))

        return res if res != inf else -1
