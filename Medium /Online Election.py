from bisect import bisect_right
from collections import defaultdict
from typing import List
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        # Store the times of votes for quick access later
        self.times = times       # List to store the leader at each time index
        self.leaders = []        # Dictionary to count votes for each person
        vote_counts = defaultdict(int)
        leader = -1               # Initialize leader and max_votes
        max_votes = 0   
        for person in persons:        # Process each vote in order
            vote_counts[person] += 1  # Increment the vote count for the current person
            # If current person's votes are >= max votes so far,
            # update the leader to this person (tie goes to most recent vote)
            if vote_counts[person] >= max_votes:
                max_votes = vote_counts[person]
                leader = person
            
            # Append current leader to the leaders list
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        # Find the index of the last vote cast at or before time t
        # bisect_right returns insertion position; subtract 1 to get actual index
        idx = bisect_right(self.times, t) - 1
        
        # Return the leader at that vote index
        return self.leaders[idx]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
