from __future__ import annotations
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
        



if __name__ == "__main__":
    def main():
        example_data = [
            ([[1,2,3],[3,2,1]], 6),
            ([[1,5],[7,3],[3,5]], 10),
            ([[2,8,7],[7,1,3],[1,9,5]], 17),
        ]

        s = Solution()

        for input_data, expected_output in example_data:
            print(f"Input:\t{input_data}")
            print(f"Expect:\t{expected_output}")
            print(f"Actual:\t{s.maximumWealth(input_data)}")
            print()


    main()
