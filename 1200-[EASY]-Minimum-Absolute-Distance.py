from collections import defaultdict
from math import inf


class Solution:
    """
    Intuition:
        We sort the array to minimize the elements wit respect
        to their neighbors. This also sets up our fixed sliding
        window approach later.

        E.g. [4, 1, 2] vs [1, 2, 4]

        Once the array is sorted, we can use a hasmap with the
        key representing the distance between 2 values. We then
        go through every pair of elements using a fixed window
        of size 2 and compute the distance. We also keep track
        of the min distance to return our final result.

    Runtime:
        Sorting the array takes O(n * log n).

        Building the hashmap takes O(n).

        Overall O(n * log n) time.

    Memory:
        Sorting in place costs O(n) in the worst case (according
        to Gemini quick summary...).

        The hashmap takes O(n) space.

        Overall, O(n) space.
    """

    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        minDiff = inf

        # hashmap -- key on diff
        hashmap: defaultdict[int, list[list[int]]] = defaultdict(list)
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i + 1]
            diff = abs(a - b)
            hashmap[diff].append([a, b])

            if diff < minDiff:
                minDiff = diff

        return hashmap[minDiff]
