class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.size = size
        return None

    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x: int, y: int) -> None:
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.root[ry] = rx
            self.size -= 1
    
    def get_size(self) -> int:
        return self.size

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)
        
        return uf.get_size()