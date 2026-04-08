class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsc = nums.copy()
        numsc.extend(nums)
        return numsc
        