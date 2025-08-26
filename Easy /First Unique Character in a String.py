class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        # Solution 1
        # for index,char in enumerate(s):
        #     if char in dict1:
        #         dict1[char] = [dict1[char][0] + 1 , index]
        #     else:
        #         dict1[char] = [1,index]
        # que = deque(s)
        # while que:
        #     front_val =que.popleft()
        #     if dict1[front_val][0] == 1:
        #         return  dict1[front_val][1]
        # return -1
        # Solution 2
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        for index,char in enumerate(s):
            if dict1[char] == 1:
                return index
        return -1
        
