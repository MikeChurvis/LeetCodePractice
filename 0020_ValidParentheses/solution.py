# [CRITICAL] an open bracket MUST be followed by its 
# corresponding close bracket.
brackets = "(){}[]"

class Solution:
    def isValid(self, s: str) -> bool:
        close_bracket_stack = []

        for char in s:
            
            # [NOTE] A problem constraint guarantees that 
            # `char in brackets` is always True.
            char_index = brackets.index(char)
            char_is_open_bracket = char_index % 2 == 0

            # Open brackets push their matching close bracket to the stack.
            if char_is_open_bracket:
                matching_close_bracket = brackets[char_index + 1]
                close_bracket_stack.append(matching_close_bracket)
            
            # A matching close bracket pops the stack.
            elif len(close_bracket_stack) and close_bracket_stack[-1] == char:
                close_bracket_stack.pop()

            # A non-matching close bracket is invalid.
            else:
                return False

        # If the stack is now empty, all brackets matched.
        if len(close_bracket_stack) == 0:
            return True

        return False


if __name__ == "__main__":
    def main():
        example_data = [
            ("()", True),
            ("()[]{}", True),
            ("(]", False)
        ]

        solution = Solution()

        for datum in example_data:
            input_data, expected_output = datum
            actual_output = solution.isValid(input_data)

            print(f"Input:\t{input_data}")
            print(f"Expect:\t{expected_output}")
            print(f"Actual:\t{actual_output}")
            print()



    main()
