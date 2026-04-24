class Solution:
    def _pif(self, a: int, b: int) -> float:
        return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for a in points:
            heapq.heappush(heap, (self._pif(a[0], a[1]), a))
        
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res