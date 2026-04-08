class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            idx = (start + end) // 2
            num = nums[idx]
            if num < target:
                start += 1
            elif num > target:
                end -= 1
            else:
                return idx
        return -1