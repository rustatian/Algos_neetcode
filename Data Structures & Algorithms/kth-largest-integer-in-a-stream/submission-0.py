class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.h = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        for i in range(len(self.h) - self.k):
            heapq.heappop(self.h)
        return self.h[0]
        
