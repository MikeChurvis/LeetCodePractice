from typing import Optional
from definitions import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        if list1.val < list2.val:
            merged_list_head = list1
            unmerged_list_head = list2
        else:
            merged_list_head = list2
            unmerged_list_head = list1

        current_node_in_merged_list = merged_list_head

        while unmerged_list_head is not None:
            
            # If the end of the merged list tail has been reached, 
            # append all remaining unmerged nodes.
            if current_node_in_merged_list.next is None:
                current_node_in_merged_list.next = unmerged_list_head
                break

            # Advance the merged list pointer until the next node's value is 
            # greater than the value of the unmerged list head. 
            if current_node_in_merged_list.next.val <= unmerged_list_head.val:
                current_node_in_merged_list = current_node_in_merged_list.next
                continue

            # When the next merged list node's value is greater than the unmerged list 
            # head's value, it's time to swap the merged list's tail with the unmerged 
            # list's head.
            current_node_in_merged_list.next, unmerged_list_head = unmerged_list_head, current_node_in_merged_list.next

        return merged_list_head
                



if __name__ == "__main__":
    def main():
        example_data = [
            (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
            (([], []), []),
            (([], [0]), [0])
        ]

        solver_fn = Solution().mergeTwoLists

        for args, expected_output in example_data:
            actual_output = ListNode.to_values_list(solver_fn(*map(ListNode.from_values_list, args)))
                        
            print(f"Input:\t{args}")
            print(f"Expect:\t{expected_output}")
            print(f"Actual:\t{actual_output}")
            print()

    main()
