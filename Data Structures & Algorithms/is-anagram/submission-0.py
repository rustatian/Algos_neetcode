class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        res: dict[str, int] = {}
        for i, x in enumerate(s):
            val = res.get(s[i], 0)
            val-=1
            res.update({s[i]: val})
            val2 = res.get(t[i], 0)
            val2+=1
            res.update({t[i]: val2})

        for xx in res.values():
            if xx != 0:
                return False
        return True