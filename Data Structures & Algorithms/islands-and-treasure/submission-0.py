class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visited = set()
            dist = 0
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    if (row >= len(grid) or
                        col >= len(grid[0]) or
                        row < 0 or
                        col < 0 or
                        (row, col) in visited or
                        grid[row][col] == -1):
                        continue

                    elif grid[row][col] == 0:
                        return dist

                    visited.add((row, col))
                    for dr, dc in directions:
                        nr, nc = row+dr, col+dc
                        q.append((nr, nc))
                        
                dist += 1

            return INF

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    grid[r][c] = bfs(r, c)
        
            