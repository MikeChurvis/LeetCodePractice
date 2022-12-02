class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps_taken = 0

        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

            steps_taken += 1

        return steps_taken


if __name__ == "__main__":
    def main():
        example_data = [
            (14, 6),
            (8, 4),
            (123, 12)
        ]

        s = Solution()

        for input_data, expected_output in example_data:
            print(f"Input:\t{input_data}")
            print(f"Expect:\t{expected_output}")
            print(f"Actual:\t{s.numberOfSteps(input_data)}")
            print() 

    main()