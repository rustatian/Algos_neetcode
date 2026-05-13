class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.max_rank = 0

    def find(self, x: int) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x: int, y: int):
        xf = self.find(x)
        yf = self.find(y)

        if xf != yf:
            if self.rank[xf] > self.rank[yf]:
                self.root[xf] = yf
                self.rank[xf] += self.rank[yf]
                self.max_rank = max(self.max_rank, self.rank[xf])
            elif self.rank[xf] < self.rank[yf]:
                self.root[yf] = xf
                self.rank[yf] += self.rank[xf]
                self.max_rank = max(self.max_rank, self.rank[yf])
            else:
                self.rank[xf] = yf
                self.rank[xf] += self.rank[yf]
                self.max_rank = max(self.max_rank, self.rank[xf])
    
    def max_rankk(self) -> int:
        return self.max_rank



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 0:
            return 1
        uf = UnionFind(len(nums))

        nids = {n:i for i, n in enumerate(nums)}
        nset = set(nums)

        for i, n in enumerate(nset):
            if n + 1 in nids:
                uf.union(i, i+1)

        return uf.max_rankk()
        