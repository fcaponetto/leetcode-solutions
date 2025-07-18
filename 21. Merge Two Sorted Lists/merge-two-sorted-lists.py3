# 21. Merge Two Sorted Lists (1/2/57515)
# Runtime: 0 ms (98.43%) Memory: 17.82 MB (20.01%) 

# Time Complexity O(n+m) where n and m are the size of the two lists
# Space Complexity O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ###########################
        # Recursive solution
        ###########################

        def sorter(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1

            if l1.val <= l2.val:
                l1.next = sorter(l1.next, l2)
                return l1
            else:
                l2.next = sorter(l1, l2.next)
                return l2

        return sorter(list1, list2)

        ###########################
        # Iterative solution
        ###########################
        
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1

        # # Determine the head
        # if list1.val <= list2.val:
        #     head = list1
        #     list1 = list1.next
        # else:
        #     head = list2
        #     list2 = list2.next

        # curr = head

        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         curr.next = list2
        #         list2 = list2.next

        #     curr = curr.next

        # if list1:
        #     curr.next = list1
        # else:
        #     curr.next = list2

        # return head
            


        