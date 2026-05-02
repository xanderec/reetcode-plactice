class Solution:
    """
    Intuition:
        Brute force approach. Linear scan over all numbers in the interval
        and check individual digits.

    Runtime:
        O(n * k) where n is the input and k is the number of digits of the
        greatest number within range. Constraint specifies upper bound of
        n to be 10^4, so 5 digits at most -> O(5n).

    Memory:
        O(1).
    """

    def rotatedDigits(self, n: int) -> int:
        res = 0
        rotateMap = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}

        for i in range(1, n + 1):
            num = i
            rotatedNum = 0
            exp = 0

            while num:
                digit = num % 10
                if digit in [3, 4, 7]:
                    break  # exit early
                num = num // 10

                rotatedDigit = rotateMap[digit]
                rotatedNum += rotatedDigit * (10**exp)
                exp += 1

            # only incr if num fully rotated
            # and input != rotated output
            if not num and i != rotatedNum:
                res += 1

        return res
