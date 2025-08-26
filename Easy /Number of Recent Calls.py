class RecentCounter(object):

    def __init__(self):
        self.q1 = deque()        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q1.append(t)
        while self.q1[0] < t - 3000 or self.q1[0] > t:
            self.q1.popleft()

        return len(self.q1)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
