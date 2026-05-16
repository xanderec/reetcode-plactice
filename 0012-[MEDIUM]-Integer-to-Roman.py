class Solution:
    """
    Intuition:
        We maintain a stack to build our Roman numeral. We use a greedy approach
        by subtracting the largest amount until we can't. To tackle the special
        subtractive form cases, we check for when we have a count of 4. We then
        need to further distinguish between cases like IV and IX. To do so, we
        simply check if the top element of the stack is on the same order of
        magnitude or not.

    Runtime:
        O(1) given constraint on input num by problem. Would be more complicated
        if we were to generalize...

    Memory:
        O(1) given constraints, general memory would be a bit more complex...
    """

    def intToRoman(self, num: int) -> str:
        hmap = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        stack = []

        for amt in [1000, 500, 100, 50, 10, 5, 1]:
            cnt = 0
            while amt <= num:
                num -= amt
                cnt += 1

            # encounter need for subtractive form
            if cnt == 4:
                # case we need to form 9, 90 or 900
                if stack and stack[-1] == hmap[amt * 5]:
                    stack.pop()
                    stack.append(hmap[amt])
                    stack.append(hmap[amt * 10])
                # case we need to form 4, 40 or 400
                else:
                    stack.append(hmap[amt])
                    stack.append(hmap[amt * 5])
            # regular case
            else:
                for _ in range(cnt):
                    stack.append(hmap[amt])

        return "".join(stack)
