# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head
        carry = 0
        while l1 and l2:
            sum_l1_l2 = l1.val + l2.val + carry
            if sum_l1_l2 >= 10:
                carry = sum_l1_l2 // 10
                sum_l1_l2 = sum_l1_l2 - 10
            else:
                carry = 0

            l1 = l1.next
            l2 = l2.next
            dummy.next = ListNode(sum_l1_l2)
            dummy = dummy.next

        while l1:
            sum_l1 = l1.val + carry
            if sum_l1 >= 10:
                carry = sum_l1 // 10
                sum_l1 = sum_l1 - 10
            else:
                carry = 0
            dummy.next = ListNode(sum_l1)
            dummy = dummy.next
            l1 = l1.next

        while l2:
            sum_l2 = l2.val + carry
            if sum_l2 >= 10:
                carry = sum_l2 // 10
                sum_l2 = sum_l2 - 10
            else:
                carry = 0
            dummy.next = ListNode(sum_l2)
            dummy = dummy.next
            l2 = l2.next
        
        if l1 is None and l2 is None and carry > 0:
            dummy.next = ListNode(carry)

        return head.next

