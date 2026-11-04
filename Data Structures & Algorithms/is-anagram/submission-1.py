class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = []
        seen2 = [] 
        for i in s: 
            seen1.append(i)
        for j in t: 
            seen2.append(j)
        seen1.sort() 
        seen2.sort()
        if seen1 == seen2:
            return True
        return False