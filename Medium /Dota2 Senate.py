class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        dire = deque()
        radiant = deque()

        senate_list = list(senate )

        for index,char in enumerate(senate_list):
            if char == "R":
                radiant.append(index)
            else:
                dire.append(index)



        while dire and radiant:
            d_val = dire.popleft() 
            r_val = radiant.popleft()

            if r_val < d_val:
                radiant.append(r_val + len(senate_list))
            else:
                dire.append(d_val+len(senate_list))

        if radiant:
            return "Radiant"
        else:
            return "Dire"
