# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key =  key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        import copy as cp
        pp: list[list[Pair]] = []
        for i in range(len(pairs)):
            key = pairs[i]
            j = i - 1

            while j >= 0 and key.key < pairs[j].key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = key
            pp.append(cp.copy(pairs))

        return pp
