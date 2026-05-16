class Solution:
    """
    Intuition:
        The intuition remains vastly the same as the previous version
        of this question (leetcode #153). The crux of this problem is
        how to tackle duplicates.

        The addition we introduce is to skip duplicates at either sides
        of the interval bounded by the l & r ptrs. By eliminating these
        duplicates, we remove the ambiguity and can easily determine if
        either partition is properly sorted.

    Runtime:
        O(n) since in the worst case, we have an array containing only
        duplicates.

    Memory:
        O(1) since we only use ptrs.
    """

    def findMin(self, nums: list[int]) -> int:
        N = len(nums)

        l, r = 0, N - 1
        while l < r:
            # adjust left and right ptrs to skip duplicates
            while l < N - 1 and nums[l] == nums[l + 1]:
                l += 1

            while r > 0 and nums[r] == nums[r - 1]:
                r -= 1

            # binary search sequence
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
