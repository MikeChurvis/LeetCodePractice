from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        value_stack = []

        current_node = head
        while True:
            value_stack.append(current_node.val)
            if current_node.next is None:
                break
            current_node = current_node.next

        current_node = head
        for i in range(len(value_stack) // 2):
            if value_stack.pop() != current_node.val:
                return False
            current_node = current_node.next

        return True


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
