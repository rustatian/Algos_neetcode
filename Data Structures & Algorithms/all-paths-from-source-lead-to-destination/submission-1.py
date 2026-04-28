class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node: int) -> bool:
            if not adjl[node]:
                return node == destination

            if node in memo:
                return memo[node]
            
            for neighbor in adjl[node]:
                if neighbor in seen:
                    return False
                seen.add(neighbor)
                if not dfs(neighbor):
                    return False
                seen.remove(neighbor)
            memo[node] = True
            return True

        adjl = [[] for _ in range(n)]
        for s, d in edges:
            adjl[s].append(d)

        seen = set()
        memo = {}

        return dfs(source)