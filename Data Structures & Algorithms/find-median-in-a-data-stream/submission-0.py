import heapq

class MedianFinder:

    def __init__(self):
        self.mxh = []
        self.mih = []

    def addNum(self, num: int) -> None:
        # if k = 2*n+1 -> lo allowed to hold n + 1, while hi - n
        # if k = 2 * n -> lo and hi ballanced with n elements each
        heapq.heappush_max(self.mxh, num)
        mx = heapq.heappop_max(self.mxh)
        heapq.heappush(self.mih, mx)

        if len(self.mih) > len(self.mxh):
            mi = heapq.heappop(self.mih)
            heapq.heappush_max(self.mxh, mi)

    def findMedian(self) -> float:
        if len(self.mxh) > len(self.mih):
            return self.mxh[0]
        
        return (self.mxh[0] + self.mih[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()