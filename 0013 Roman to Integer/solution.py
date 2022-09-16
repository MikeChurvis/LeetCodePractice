roman_numeral_letter_values = {
    'I': 1, 
    'V': 5, 
    'X': 10, 
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total_value_of_numeral = 0
        
        # Reverse the numeral to parse it in ascending order.
        numeral = reversed(s)
        
        # Maintain a register of the greatest value parsed so far.
        greatest_value_parsed = 0
        
        for current_letter in numeral:
            current_value = roman_numeral_letter_values[current_letter]
            
            # Subtract the current value from the total if it precedes a greater value.
            # (examples: IV = 5 - 1, XC = 100 - 10, CM = 1000 - 100, ...)
            if current_value < greatest_value_parsed:
                total_value_of_numeral -= current_value
                
            # Otherwise, accumulate the value.
            else:
                total_value_of_numeral += current_value
                greatest_value_parsed = current_value
            
            
                
        return total_value_of_numeral
            