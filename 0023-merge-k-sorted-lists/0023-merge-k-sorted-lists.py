# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= new = ListNode()
        
        while(list1 and list2):
            if list1.val < list2.val:
                new.next = list1
                list1 = list1.next
            else:
                new.next = list2
                list2 = list2.next
            new = new.next
        
        if list1:
            new.next = list1
        else:
            new.next = list2 
        
        return dummy.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            nodes = []
            h = p = ListNode()
            for l in lists:
                while l:
                    heapq.heappush(nodes, l.val)
                    l = l.next
            while nodes:
                p.next = ListNode(heapq.heappop(nodes))
                p = p.next
            return h.next







