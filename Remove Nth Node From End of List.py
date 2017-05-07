# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = ListNode(0)
        second = ListNode(0)
        second.next = head
        first.next = head
        res = first
        for _ in range(n + 1):
            second = second.next
        while second is not None:
            first = first.next
            second = second.next
        first.next = first.next.next

        return res.next