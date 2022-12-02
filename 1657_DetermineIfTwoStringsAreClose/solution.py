class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Words must be equal in length.
        if len(word1) != len(word2):
            return False

        # Words must contain the same set of characters.
        letters = set(word1)
        if letters != set(word2):
            return False

        # Find how many of each letter is in the word.
        word_1_letter_counts = {letter: 0 for letter in letters}
        word_2_letter_counts = {letter: 0 for letter in letters}

        for letter in word1:
            word_1_letter_counts[letter] += 1
        for letter in word2:
            word_2_letter_counts[letter] += 1

        # Each letter is a group. The count of each letter is the
        # size of the group. Size is a property of a group. Groups can
        # swap their size property using Operation 2. Therefore, as long
        # as both word share the same collection of group sizes, the words
        # can be changed into one another.
        word_1_counts = sorted(word_1_letter_counts.values())
        word_2_counts = sorted(word_2_letter_counts.values())

        if word_1_counts != word_2_counts:
            return False

        # Passing all of the above checks guarantees that a solution exists.
        return True


if __name__ == "__main__":
    def main():
        example_data = [
            # (input, expected_output),
            (("abc", "bca"), True),
            (("a", "aa"), False),
            (("cabbba", "abbccc"), True),
            (("god", "dog"), True),
            (("cabbbb", "abbccc"), False),
        ]

        solver_fn = Solution().closeStrings

        for datum in example_data:
            input_data, expected_output = datum
            actual_output = solver_fn(*input_data)

            print(f"Input:\t{input_data}")
            print(f"Expect:\t{expected_output}")
            print(f"Actual:\t{actual_output}")
            print()

    main()
