class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rc = [0] * len(picture)
        cc = [0] * len(picture[0])

        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j] == "B":
                    rc[i]+=1
                    cc[j]+=1
        
        res = 0

        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j] == "B" and rc[i] == 1 and cc[j] == 1:
                    res+=1
        
        return res