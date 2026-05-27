class Solution:
    """
    Intuition:
        Initialize a bitmap for lower and uppercase chars.

        Iterate through the word and flip respective bits.

        At the end, we perform an element-wise AND join
        and return the sum which takes true = 1 and false = 0.

    Runtime:
        O(n) for the linear pass on 'word'.

    Memory:
        O(1) since the bitmaps are each bounded at 26 elmts.
    """

    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26

        for char in word:
            if char.islower():
                lower[ord(char) - ord("a")] = True
            else:
                upper[ord(char.lower()) - ord("a")] = True

        res = [a and b for a, b in zip(lower, upper)]
        return sum(res)
