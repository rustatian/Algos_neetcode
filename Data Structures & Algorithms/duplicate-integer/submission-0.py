class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = {}
        for num in nums:
            if num in sett:
                return True
            else:
                sett[num] = "foo"
        return False
         