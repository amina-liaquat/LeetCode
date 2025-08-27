class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,-nums[i])
        
        top=0
        for i in range(k):
            top=heapq.heappop(heap)

        return -top
        
