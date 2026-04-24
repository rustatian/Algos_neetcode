class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        if len(nums) == k:
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count, key=count.get)