class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") >= 2 :
            return False
            
                
        count = 0
        for i in range(len(s)):
                    
            if s[i] == "L" :
                count += 1
                if count == 3:
                    return False
            else:
    
                count = 0
        return True
