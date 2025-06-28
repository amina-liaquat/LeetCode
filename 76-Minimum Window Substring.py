class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #empty string
        res = ""
        min_left = min_right = -1

        if len(s) < len(t):
            return res

        min_len = float('inf') # maximum positive number

        # map of required characters
        need = {}
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1

        # map of characters with count = 0
        window = {}
        for i in t:
            window[i] = 0

        #counter
        have = 0 #this one will be maintained

        #the total length of the window
        required = len(t) # the length of t

        #pointers
        left, right = -1, 0

        while right < len(s) and left <= len(s) - required:
            #update right
            if s[right] not in need:
                right += 1
            else:
                #first time only
                if have == 0:
                    left = right
                #update window
                window[s[right]] += 1
                # update have if only
                if window[s[right]] <= need[s[right]]:
                    have += 1
                    while have == required:
                        potential_min_len = abs(left - right) + 1
                        if potential_min_len < min_len:
                            # res  = s[left: right+1]
                            min_left = left
                            min_right = right + 1
                            min_len = potential_min_len

                     #update the left by one char and also update the window and have
                        window[s[left]] -= 1
                        if window[s[left]] < need[s[left]]:
                            have -= 1
                        left += 1
                        
                        #move left until one char found
                        while left < len(s) - required:
                            if s[left] not in need:
                                left += 1
                            else:
                                break
                right += 1

        # return res
        return s[min_left: min_right]
