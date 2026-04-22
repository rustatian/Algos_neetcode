class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] > nums[mid + 1] and nums[mid] <= nums[mid - 1]:
                hi = mid
            else:
                lo = mid + 1
        return lo