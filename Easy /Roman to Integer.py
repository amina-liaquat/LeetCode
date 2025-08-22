class Solution:
  def romanToInt(self, s: str) -> int:
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    
    for char in s:
        
        value = roman_to_int[char]
        
        
        if prev_value < value:
            total += value - 2 * prev_value
        else:
            total += value
        
      
        prev_value = value
    
    return total
    
