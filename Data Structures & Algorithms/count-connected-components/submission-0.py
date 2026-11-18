class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbor = collections.defaultdict(list)
        for edge in edges:
            neighbor[edge[0]].append(edge[1])
            neighbor[edge[1]].append(edge[0])


        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in neighbor[node]:
                if nei not in visited:
                    dfs(nei)
            
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
        