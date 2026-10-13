class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visit = set()
        adj = [[] for _ in range(n)]

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)

        for node in range(n):
            if node not in visit:
                res += 1
                dfs(node)
        return res