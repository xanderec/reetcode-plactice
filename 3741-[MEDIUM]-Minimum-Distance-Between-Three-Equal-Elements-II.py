from collections import defaultdict
from math import inf


class Solution:
    """
    Intuition:
        See intuition for problem 3740, Solution 2 & 3.

    Runtime:
        O(n) to build hashmap.

        O(n) to traverse through all indices for a given
        distance.

        Overall, O(n) time.

    Memory:
        O(n) for the hashmap.
    """

    def minimumDistance(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return -1

        # build hashmap -- key on value
        hashmap: defaultdict[int, list[int]] = defaultdict(list)
        for ix, n in enumerate(nums):
            hashmap[n].append(ix)

        # compute min dist of good tuple
        minDist = inf
        for indices in hashmap.values():
            # can't form a good tuple
            if len(indices) < 3:
                continue

            # fixed sliding window -- size 3
            for l in range(len(indices) - 2):
                r = l + 2
                dist = abs(indices[l] - indices[r]) * 2

                if dist < minDist:
                    minDist = dist

        return minDist if minDist != inf else -1
