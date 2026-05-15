class Solution:
    """
    Intuition:
        Use an index to traverse the string and divide parsing into
        phases: whitespaces, pos/neg sign, extract numerical value.

    Runtime:
        O(n) since we process each char up to once.

    Memory:
        O(1).
    """

    def myAtoi(self, s: str) -> int:
        N = len(s)
        ix = 0

        # leading whitespaces
        while ix < N and s[ix] == " ":
            ix += 1

        # consume pos/neg sign
        sign = 1  # implicitly positive
        if ix < N and s[ix] in "-+":
            sign = -1 if s[ix] == "-" else 1
            ix += 1

        # parse numerical val
        num = 0
        while ix < N:
            if not s[ix].isdigit():
                break

            digit = int(s[ix])
            num = num * 10 + digit
            ix += 1

        # adjust if overflow
        if sign == -1 and num > 2**31:
            num = 2**31
        if sign == 1 and num > 2**31 - 1:
            num = 2**31 - 1

        return sign * num
