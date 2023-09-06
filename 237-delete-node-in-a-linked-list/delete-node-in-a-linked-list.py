class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next

#node.val = node.next.val: This line updates the value of the current node (the one you want to delete) with the value of the next node. This essentially makes the current node's value equal to the value of the next node. It's a way to "copy" the value of the next node into the current node.
       