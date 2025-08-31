class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in group:
                group[key].append(i)
            else:
                group[key] = [i]
        return list(group.values())
