class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we need a way to track what has been seen so lets make a set since sets are faster
        seen = set() 
        # iterate through the list of nums and take each value
        for num in nums: 
            if num in seen: 
                return True
            seen.add(num) # add the value to the seen
        return False 