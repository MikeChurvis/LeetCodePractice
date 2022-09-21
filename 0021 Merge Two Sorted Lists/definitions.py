from __future__ import annotations
from typing import Optional
from functools import reduce


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_values_list(cls, values: list) -> Optional[ListNode]:
        return reduce(
            lambda head, val: cls(val, head),
            reversed(values),
            None
        )

    @classmethod
    def to_values_list(cls, head: Optional[ListNode]) -> list[int]:
        values = []
        current_node = head
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next
        return values


if __name__ == "__main__":
    def main():
        test_list = ListNode.from_values_list([1, 2, 3])

        while test_list is not None:
            print(test_list.val)
            test_list = test_list.next

    main()
