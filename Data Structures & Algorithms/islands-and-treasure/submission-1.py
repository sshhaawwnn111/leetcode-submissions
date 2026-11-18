class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        q = deque()
        visited = set()

        def addCell(r, c):
            if r < len(grid) and r >= 0 and c < len(grid[0]) and c >= 0 and (r, c) not in visited and grid[r][c] > 0:
                q.append((r,c))
                visited.add((r,c))



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    addCell(nr, nc)

            dist += 1

        
            