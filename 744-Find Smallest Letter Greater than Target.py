class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        while left<=right:
            mid=(left+right)//2
            if target >= letters[mid]:
                left=mid+1
            else:
                right=mid-1
        return letters[left]  if left < len(letters)  else letters[0]    
