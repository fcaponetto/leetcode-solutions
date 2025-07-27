# 23. Merge k Sorted Lists (6/8/57540)
# Runtime: 17 ms (95.00%) Memory: 21.46 MB (0.00%) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Simple approach
# Time Complexity O(k * (m + n)) where m and n are the length of the two lists
# Space Complexity O(1)

# Divide and Conquer
# Time Complexity O(n log k) where the n=number of nodes and k= number of steps (lists)
# Space Complexity O(k)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # The mergeList function returns the head of the merged list
        def mergeList(node1, node2):

            if not node1:
                return node2
            if not node2:
                return node1

            if node1.val <= node2.val:
                node1.next = mergeList(node1.next, node2)
                return node1
            else:
                node2.next = mergeList(node1, node2.next)
                return node2


        if not lists:
            return None


        # Simple approach - Inefficient
        # if len(lists) == 1 then return the only available list (no for loop)
        # head = lists[0]
        # for i in range(1, len(lists)):
        #     head = mergeList(head, lists[i])
        # return head


        # Divide and Conquer
        # It merges lists in pairs during each iteration

        while len(lists) > 1:
            # To store the results of merging pairs in the current iteration.
            tmpMergedLists = []

            for i in range(0, len(lists), 2):
                node1 = lists[i]
                node2 = lists[i+1] if (i+1) < len(lists) else None
                tmpMergedLists.append(mergeList(node1, node2))
            lists = tmpMergedLists

        return lists[0]
