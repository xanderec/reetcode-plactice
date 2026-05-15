class Solution:
    """
    Intuition:
        Cast int to array of chars and use built-in functions
        to compare array to reversed form.

    Runtime:
        O(n) for casting and reversing.

    Memory:
        O(n) for the arrays.
    """

    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))
        return s == s[::-1]
