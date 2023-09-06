# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        st = set()
        while headA:
            st.add(headA)
            headA = headA.next
        while headB:
            if headB in st:
                return headB
            headB = headB.next
        return None
#we need to compare the  address of every pointer not value in linked lists

'''while headB != None:
            temp = headA
            while temp != None:
                if temp == headB:
                    return headB
                temp = temp.next
            headB = headB.next
        return None'''