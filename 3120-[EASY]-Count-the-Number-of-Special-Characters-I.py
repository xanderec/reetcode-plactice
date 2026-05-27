class Solution1:
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


class Solution2:
    """
    Intuition:
        Hash the chars in the input word and iterate over them
        by checking both variants and seeing if they are both
        present.

    Runtime:
        O(n) to hash.

    Memory:
        O(1) given that we have at most 26 * 2 letters in our
        hash set.
    """

    def numberOfSpecialChars(self, word: str) -> int:
        letters = set(word)
        res = set()

        for letter in letters:
            if (
                letter.lower() in letters
                and letter.upper() in letters
                and letter.lower() not in res
            ):
                res.add(letter.lower())

        return len(res)


class Solution3:
    """
    Intuition:
        Hashset oriented approach as well, except we change the loop
        to go over all letters in the alphabet.

    Runtime:
        Still O(n).

    Memory:
        Still O(1).
    """

    def numberOfSpecialChars(self, word: str) -> int:
        letters = set(word)
        res = 0

        for letter in "abcdefghijklmnopqrstuvwxyz":
            if letter in letters and letter.upper() in letters:
                res += 1

        return res
