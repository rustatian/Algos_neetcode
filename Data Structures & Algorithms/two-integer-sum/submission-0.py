class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d: dict[int, int] = {}

        for i, x in enumerate(nums):
            if math.fabs(target - x) in d:
                answ = list((i, d[math.fabs(target - x)]))
                answ.sort()
                return answ
            else:
                d.update({x:i})
        return list((0, 0))

        