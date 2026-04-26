# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def size_ll(self, head):
        temp = head
        n = 0
        while temp:
            n += 1
            temp = temp.next
        return n

    def reverse_ll(self, head):
        if head is None or head.next is None:
            return head

        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
    def print_ll(self, head):
        while head:
            print(head.val)
            head = head.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next:
            size_of_ll = (self.size_ll(head) // 2) - 1
            curr = head
            while size_of_ll:
                curr = curr.next
                size_of_ll -= 1

            r_head = self.reverse_ll(curr.next)
            curr.next = None

            temp = None
            r_temp = None
            while head.next:
                temp = head.next
                head.next = r_head
                head = temp
                r_temp = r_head.next
                r_head.next = temp
                r_head = r_temp
            
            head.next = r_head
            

        