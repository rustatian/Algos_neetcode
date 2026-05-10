class UnionFind:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x: int, y: int) -> None:
        xf = self.find(x)
        yf = self.find(y)
        if self.rank[xf] > self.rank[yf]:
            self.root[yf] = xf
            self.rank[xf] += self.rank[yf]
        elif self.rank[xf] < self.rank[yf]:
            self.root[xf] = yf
            self.rank[yf] += self.rank[xf]
        else:
            self.root[yf] = xf
            self.rank[xf] += self.rank[yf]
    
    def max_rank(self) -> int:
        mr = 0
        for r in self.rank:
            mr = max(mr, r)
        return mr



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(len(nums))
        sn = set(nums)
        normalize = {n:i for i, n in enumerate(sn)}

        for i, n in enumerate(sn):
            if n + 1 in normalize:
                uf.union(i, normalize[n+1])

        return uf.max_rank()
        