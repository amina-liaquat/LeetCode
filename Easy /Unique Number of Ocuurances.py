class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_dict = {}

        for i in range(len(arr)):
            if arr[i] in my_dict:
                my_dict[arr[i]] += 1
            else:
                my_dict[arr[i]] = 1

        distinct = my_dict.values()
        my_set = set(distinct)

        return len(distinct) == len(my_set)
        
