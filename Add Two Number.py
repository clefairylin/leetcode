# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = ''
        while True:
            num1 = str(l1.val) + num1
            if not l1.next:
                break
            l1 = l1.next
        while True:
            num2 = str(l2.val) + num2
            if not l2.next:
                break
            l2 = l2.next
        result = str(int(num1) + int(num2))
        l3 = ListNode(int(result[0]))
        for i in result[1:]:
            l = ListNode(int(i))
            l.next = l3
            l3 = l
        return l3