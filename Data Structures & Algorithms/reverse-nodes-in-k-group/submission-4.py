# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth_node = self.getNode(groupPrev, k)
            if not kth_node:
                break
            groupNext = kth_node.next

            prev = kth_node.next
            curr = groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth_node
            groupPrev = temp
        return dummy.next
    
    def getNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next 
            k -= 1
        return curr


            


        