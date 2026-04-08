class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        res =[[0]*len(mat2[0]) for _ in range(len(mat1))]

        for ri, rels in enumerate(mat1):
            for ei, rel in enumerate(rels):
                if rel:
                    for ci, ce in enumerate(mat2[ei]):
                        res[ri][ci] += rel*ce

        return res