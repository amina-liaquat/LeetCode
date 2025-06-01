class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        output = str(s[:])
        shift = 0
        
        for index, source, target in sorted(zip(indices, sources, targets)):
            if s[index:index+len(source)] == source:
                index += shift

                output = output[:index] + target + output[index+len(source):]
                shift += len(target) - len(source)
        
        return output
