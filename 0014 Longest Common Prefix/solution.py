from __future__ import annotations
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""

        # Group the letters of each word by their position in
        # the word (1st letter, 2nd, 3rd, ...), then convert
        # each group into a set to remove duplicate letters.
        # A set with exactly one letter means that all words 
        # share the same letter at that set's position.
        letter_sets_by_position = map(set, zip(*strs))

        for letter_set in letter_sets_by_position:
            if len(letter_set) > 1:
                break

            common_prefix += letter_set.pop()

        return common_prefix
            


if __name__ == "__main__":
    def main():
        example_data = [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], "")
        ]

        solution = Solution()

        for datum in example_data:
            input_data, expected_output = datum
            actual_output = solution.longestCommonPrefix(input_data)

            print(f"Input:\t{input_data}")
            print(f"Expect:\t{expected_output}")
            print(f"Actual:\t{actual_output}")
            print()



    main()
