class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = {src: [] for src, dst in tickets}
        for src, dst in tickets:
            adj[src].append(dst)

        paths = ["JFK"]

        def dfs(src: str):
            if len(paths) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = adj[src].copy()
            for i, v in enumerate(temp):
                adj[src].pop(i)
                paths.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                paths.pop()
            return False

        dfs("JFK")
        return paths
