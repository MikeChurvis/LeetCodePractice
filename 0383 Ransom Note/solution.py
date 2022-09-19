class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Accumulate the character counts in magazine.
        magazine_char_counts = {}

        for char in magazine:
            magazine_char_counts[char] = (magazine_char_counts.get(char) or 0) + 1

        # Withdraw each character in ransomeNote from the ones available in magazine.
        for char in ransomNote:
            char_count = magazine_char_counts.get(char)

            # Return false if there is no such character in magazine, or if no such characters remain.
            if char_count is None or char_count <= 0:
                return False

            magazine_char_counts[char] = char_count - 1
        
        return True