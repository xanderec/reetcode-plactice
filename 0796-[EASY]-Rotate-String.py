class Solution1:
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


class Solution2:
    """
    Intuition:
        The constructed string s + s will contain all rotated forms.
        Since we are trying to fit goal into this constructed string,
        we simply use substring matching to check.

        We also need a guard to ensure that the lengths of both inputs
        are the same.

    Runtime:
        O(2 * n) ~ O(n) to construct s + s.

        O(2 * n) ~ O(n) for substring match.

        Overall, O(n) runtime.

    Memory:
        O(2 * n) to allocate s + s string.
    """

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return goal in s + s
