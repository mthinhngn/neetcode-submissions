class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        # Each edge is treated like H1, H2, H3...
        # edge_graph[i] = other edges connected to edge i
        edge_graph = {i: [] for i in range(len(edges))}

        # Track nodes that appear in at least one edge
        used_nodes = set()

        for a, b in edges:
            used_nodes.add(a)
            used_nodes.add(b)

        # Connect edges if they share a node
        for i in range(len(edges)):
            a, b = edges[i]

            for j in range(i + 1, len(edges)):
                c, d = edges[j]

                # Edge i and edge j share a node
                if a == c or a == d or b == c or b == d:
                    edge_graph[i].append(j)
                    edge_graph[j].append(i)

        visit = set()

        def dfs(edge):
            visit.add(edge)

            for next_edge in edge_graph[edge]:
                if next_edge not in visit:
                    dfs(next_edge)

        components = 0

        # Every NEW unvisited edge starts a new component
        for edge in range(len(edges)):
            if edge not in visit:
                components += 1
                dfs(edge)

        # Nodes with no edges are their own components
        isolated_nodes = n - len(used_nodes)

        return components + isolated_nodes