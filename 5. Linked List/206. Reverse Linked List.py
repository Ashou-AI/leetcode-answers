# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Approach 1: Iteration (Tail Insertion)
    time: O(n), space: O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            # # Details:  [prev -> curr -> next] -> [prev <- curr <- next]
            # next = curr.next  # temporary variable
            # curr.next = prev
            # prev = curr
            # curr = next
        return prev


class Solution:
    """
    Approach 1.2: Iteration (Head Insertion)
    time: O(n), space: O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(next=head)
        prev, curr = dummy, dummy.next
        while curr.next:
            next = curr.next  # a)
            curr.next, next.next, prev.next = next.next, prev.next, next  # b) c) d)
            # # Details:  [prev -> curr -> next] -> [prev -> next -> curr]
            # next = curr.next  # a)
            # curr.next = next.next  # b)
            # next.next = prev.next  # c)
            # prev.next = next  # d)
        return dummy.next


class Solution:
    """
    Approach 2: Recursion
    time: O(n), space: O(n)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev
