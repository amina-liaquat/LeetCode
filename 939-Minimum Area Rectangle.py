class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = {}  # {1: [1, 3]}
        for x, y in points:
            if x not in columns:
                columns[x] = []
            columns[x].append(y)

        lastx = {}  # (1,3): 1 # seen
        ans = float("inf")

        for x in sorted(columns): 
            column = columns[x]
            column.sort()  # lesser y comes first

            for j, y2 in enumerate(column): 
                for i in range(j): 
                    y1 = column[i]

                    if (y1, y2) in lastx:
                        width = x - lastx[y1, y2]
                        height = y2 - y1
                        area = width * height
                        ans = min(area, ans)

                    lastx[y1, y2] = x

        if ans < float("inf"):
            return ans
        else:
            return 0
