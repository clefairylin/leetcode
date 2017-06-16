# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        temp = pre
        while temp.next and temp.next.next:
            node1, node2 = temp.next, temp.next.next
            temp.next, node2.next, node1.next = node2, node1, node2.next
            temp = node1
        return pre.next
