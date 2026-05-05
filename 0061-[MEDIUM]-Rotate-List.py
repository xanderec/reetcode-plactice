from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Intuition:
        Instead of iteratively rotating the linked list, we can see it
        as breaking it into 2 halves and rearranging them to get our
        final rotated form.

        To do this, we maintain fast and slow ptrs. The fast ptr gets
        a head start of 'k' jumps. The slow one trails behind. Here,
        the fast ptr represents the tail of the first half of the rotated
        linked list and the slow ptr the tail of the second half.

        We have some optimizations such as checking for an empty linked
        list and dividing 'k' by the length of our linked list and
        returning early if 'k' is 0 (effectively no rotations).

    Runtime:
        O(n) to compute the length of the LL.

        O(n) for fast/slow ptr traversals.

        Overall, O(n) runtime.

    Memory:
        O(1) since we only deal with ptrs.
    """

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # early return
        if not head or k == 0:
            return head

        # compute length
        N = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            N += 1

        k = k % N
        # early return
        if k == 0:
            return head

        fast = head
        for _ in range(k):
            fast = fast.next

        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        # store res ptr
        res = slow.next
        # modify ptrs
        slow.next = None  # break halves
        fast.next = head  # rotate

        return res
