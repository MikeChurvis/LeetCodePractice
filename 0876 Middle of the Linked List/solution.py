from typing import Optional

from definitions import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Make two pointers: tail and middle.
        
        Advance through the linked list. For every 2 steps tail 
        takes, middle takes 1. Thus, middle will always be in 
        the middle of the list insofar as it has been parsed.

        When tail reaches the end of the list, return middle's node.
        """

        tail_ptr: Optional[ListNode] = head
        middle_ptr: Optional[ListNode] = head

        while True:
            tail_ptr = tail_ptr.next
            
            if tail_ptr is None:
                break

            middle_ptr = middle_ptr.next
            tail_ptr = tail_ptr.next

            if tail_ptr is None:
                break


        return middle_ptr
        