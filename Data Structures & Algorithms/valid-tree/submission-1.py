class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbor = collections.defaultdict(list)
        for edge in edges:
            if edge[0] == edge[1]:
                return False
            neighbor[edge[0]].append(edge[1])
            neighbor[edge[1]].append(edge[0])

        cycle, visited = set(), set()

        def dfs(node):
            if node in cycle:
                return False
            
            cycle.add(node)
            visited.add(node)
            for nei in neighbor[node]:
                if nei not in visited:
                    if not dfs(nei):
                        return False
            visited.remove(node)
            return True
        
        res = dfs(0)

        return res if len(cycle) == n else False
        