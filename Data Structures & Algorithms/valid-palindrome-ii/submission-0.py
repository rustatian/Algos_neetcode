class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        sinv = s[::-1]
        return s == sinv