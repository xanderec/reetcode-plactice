class Solution:
    """
    Intution:
        Brute force approach. Slice string by every index and
        construct rotation. If we get a match, return true else
        return false.

    Runtime:
        O(n^2) since we have N steps and each step costs O(n).

    Memory:
        O(n) since we need to allocate a string at each step for
        the rotation.
    """

    def rotateString(self, s: str, goal: str) -> bool:
        N = len(s)
        for i in range(N):
            if s[i:] + s[:i] == goal:
                return True

        return False
