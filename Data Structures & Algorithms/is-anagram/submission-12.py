class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = []
        seen2 = []
        for letter in s: 
            seen1.append(letter)
        seen1.sort()
        for letter in t: 
            seen2.append(letter)
        seen2.sort()
        return seen1 == seen2