class Solution:
    """
    Intuition:
        We can view the encoded cipher text as a matrix where we have
        to traverse diagonally.

        Given the number of rows, we can compute the nunmber of cols
        to get the dimensions of our matrix.

        Then, it's a simple matter of going through all start points
        (each column slot of topmost row) and traversing diagonally
        while maintaining bounds

    Runtime:
        O(n) since we have to process each character in the encoded
        text in the worst case.

    Memory:
        We don't actually allocate space for a matrix, so we only
        need extra space to store the result which is O(n) in the
        worst case.
    """

    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        s = encodedText  # alias because I am lazy

        # early return for base cases
        if not s:
            return s

        if rows == 1:
            return s

        cols = len(s) // rows
        res = []

        for start in range(cols):
            r, c = 0, start

            while r < rows and c < cols:
                res.append(s[r * cols + c])
                r += 1
                c += 1

        return "".join(res).rstrip()
