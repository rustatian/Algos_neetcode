class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        return None

    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x: int, y: int) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            # cycles
            return False
        self.root[ry] = rx
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        uf = UnionFind(n)
        for x, y in edges:
            if not uf.union(x, y):
                return False 
        
        return True
        