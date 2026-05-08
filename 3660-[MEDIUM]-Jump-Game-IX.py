class Solution:
    """
    Intuition:
        We can think of the input as intervals or groups for which every
        elmt within a given group can jump to the same "local maxima".

        These groups are delimited by smaller values to the left and larger
        values to the right (inverse of jump rules!). Effectively, every
        elmt in the res array is the max of itself and all consecutive
        larger elmts immediately to its left.

        We use a monotonic stack (bottom = lowest, top = highest) to solve
        this problem. We push new blocks onto the stack and merge them
        if the topmost block has a value larger than our current block
        (meaning we can jump to it).

    Runtime:
        O(n) as we loop through every elmt. At each step, we push once and
        pop at most once which leads to O(1) cost. Overall runtime stays
        linear at O(n).

    Memory:
        In the worst case, each elmt forms a block in the stack (e.g.
        sorted input array), so need up to O(n) space.
    """

    def maxValue(self, nums: list[int]) -> list[int]:
        N = len(nums)
        stack = []  # block = (value, left, right)

        for i in range(N):
            currVal = nums[i]
            currLeft = i
            currRight = i

            # merge logic
            while stack and stack[-1][0] > nums[i]:
                topVal, topLeft, topRight = stack.pop()
                currVal = max(currVal, topVal)
                currLeft = topLeft

            stack.append((currVal, currLeft, currRight))

        res = [0] * N
        for i in range(len(stack)):
            for j in range(stack[i][1], stack[i][2] + 1):
                res[j] = stack[i][0]

        return res
