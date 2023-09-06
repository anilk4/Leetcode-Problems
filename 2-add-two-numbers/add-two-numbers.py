# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            val = v1 + v2 + carry
            carry = val // 10 #removes last digit and gives only(One's) carry like 6 + 4 ==> carry =  1
            val = val % 10 #update only the last digit that is in ones place ==> val = 0
            curr.next = ListNode(val)

            #update the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

'''edge cases are carry and l1 = [8], l2 = [7] then res = [5] to avoid this we taken carry also in while case if it exist then create a separate node and print [1,5]'''
