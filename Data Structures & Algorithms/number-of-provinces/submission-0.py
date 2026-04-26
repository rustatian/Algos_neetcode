class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution: 
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        conn = len(isConnected)

        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if uf.find(i) != uf.find(j) and isConnected[i][j] == 1:
                    conn -= 1
                    uf.union(i, j)

        return conn