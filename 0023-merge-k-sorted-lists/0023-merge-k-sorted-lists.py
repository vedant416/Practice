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
      
        res = []
        l1 = lists.pop() if len(lists)>0 else None
        l2 = lists.pop() if len(lists)>0 else None
        x = self.mergeTwoLists(l1, l2)
        if x:
            res.append(x)
        else:
            return None
        while True:
            if len(lists) == 0 and len(res) == 1:
                return res[0]
            l1 = lists.pop() if len(lists)>0 else None
            l2 = res.pop() if len(res)>0 else None
            x = self.mergeTwoLists(l1, l2)
            if x:
                res.append(x)
            
        return res[0]
            
            
            
            
            
            
            
        
        