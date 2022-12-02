from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            # If the current digit is not 9 then it has space to grow.
            # No further looping is necessary.
            if digits[i] != 9:
                digits[i] += 1
                break

            # Otherwise, set the digit to 0 and continue the loop into the next
            # order of magnitude.
            digits[i] = 0

        # If the for-loop never breaks then all of the digits were 9s and are now 0s.
        # Prepend a 1 to digits to increment the order of magnitude (ex: 999 -> 1000).
        else:
            digits.insert(0, 1)

        return digits


if __name__ == "__main__":
    def main():
        example_data = [
            ([1, 2, 3], [1, 2, 4]),
            ([4, 3, 2, 1], [4, 3, 2, 2]),
            ([9], [1, 0]),
        ]

        solver_fn = Solution().plusOne

        for datum in example_data:
            input_data, expected_output = datum
            actual_output = solver_fn(input_data)

            print(f"Input:\t{input_data}")
            print(f"Expect:\t{expected_output}")
            print(f"Actual:\t{actual_output}")
            print()

    main()
