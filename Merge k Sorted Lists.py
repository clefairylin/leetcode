# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for head in lists:
            while head is not None:
                res.append(head)
                head = head.next

        res = sorted(res, key=lambda node: node.val)
        for i,node in enumerate(res):
            try:
                node.next = res[i+1]
            except:
                node.next = None

        if res:
            return res[0]
        else:
            return None