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
        last = ListNode(0) 
        head = last
        carry = 0
        while l1 and l2:
            digit = l1.val + l2.val
            value = digit + carry
            carry, last = self.process(value, carry, last)
            l1 = l1.next
            l2 = l2.next

        while l1:
            value = carry + l1.val
            carry, last = self.process(value, carry, last)
            l1 = l1.next
            
        while l2:
            value = carry + l2.val
            carry, last = self.process(value, carry, last)
            l2 = l2.next
            
        if carry > 0:
            last.next = ListNode(carry)
        return head.next
    
    def process(self, value, carry, last):
        if value >= 10:
            value = value -10
            carry = 1
        else:
            carry = 0
        result = ListNode(value)
        last.next = result
        last = last.next
        return carry, last