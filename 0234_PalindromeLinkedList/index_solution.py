from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = tuple(linked_list_iterator(head))

        for left_index, left_value in enumerate(values):
            right_index = len(values) - (left_index + 1)

            if left_index >= right_index:
                break

            right_value = values[right_index]

            if left_value != right_value:
                return False

        return True


def linked_list_iterator(list_node):
    current_node = list_node

    while True:
        yield current_node.val

        if current_node.next is None:
            return

        current_node = current_node.next


if __name__ == '__main__':
    def list_to_linked_list(list_: list[int]) -> ListNode:
        current_node = None
        for element in reversed(list_):
            current_node = ListNode(element, current_node)
        return current_node

    def main():
        example_1_list_head = list_to_linked_list([1, 2, 3, 2, 1])
        example_2_list_head = list_to_linked_list([1, 2])

        print(Solution().isPalindrome(example_1_list_head))
        print(Solution().isPalindrome(example_2_list_head))

    main()
