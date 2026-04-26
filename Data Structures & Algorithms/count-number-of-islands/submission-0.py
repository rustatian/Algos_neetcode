class UnionFind:
    def __init__(self, grid: list[list[str]]):
        self.root = []
        self.count = 0
        r, c = len(grid), len(grid[0])
        for cr in range(r):
            for cc in range(c):
                if grid[cr][cc] == "1":
                    self.root.append(cr*c+cc)
                    self.count += 1
                else:
                    self.root.append(-1)
    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x
    def union(self, x: int, y: int):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.root[ry] = rx
            self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        uf = UnionFind(grid)
        r, c = len(grid), len(grid[0])

        for cr in range(r):
            for cc in range(c):
                if grid[cr][cc] != "1":
                    continue
                
                if cr - 1 >= 0 and grid[cr - 1][cc] == "1":
                    uf.union((cr - 1) * c + cc, cr * c + cc)
                if cr + 1 < r and grid[cr + 1][cc] == "1":
                    uf.union((cr + 1) * c + cc, cr * c + cc)
                if cc + 1 < c and grid[cr][cc + 1] == "1":
                    uf.union(cr * c + cc + 1, cr * c + cc)
                if cc - 1 >= 0 and grid[cr][cc - 1] == "1":
                    uf.union(cr * c + cc - 1, cr * c + cc)
        
        return uf.get_count()















        