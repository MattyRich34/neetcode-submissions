class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = sorted(s)
        seen2 = sorted(t)
        return seen1 == seen2