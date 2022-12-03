# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        prev = dummy 
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                
                #skip
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                
                prev.next = cur.next
                #inc cur
                cur = cur.next

            else:
                prev = cur
                cur = cur.next
                
        return dummy.next
    
    
       
       
        