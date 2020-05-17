# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head and head.next:
            even_head = head.next
            even_tail = even_head
        else:
            return head
        odd_tail = head



        while even_tail and even_tail.next:
            odd_tail.next = even_tail.next
            even_tail.next = even_tail.next.next
            even_tail = even_tail.next
            odd_tail = odd_tail.next
        odd_tail.next = even_head
        return head
