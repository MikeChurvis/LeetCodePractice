from typing import Optional
from definitions import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: 
            return list2

        if list2 is None:
            return list1
            
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        head = list1

        while True:
            if list1.next is None:
                list1.next = list2
                break

            if list1.next.val <= list2.val:
                list1 = list1.next
                continue

            list1.next, list2 = list2, list1.next

        return head
                



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
