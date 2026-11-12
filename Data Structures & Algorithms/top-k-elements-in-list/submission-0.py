class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for numbers in nums:
            if numbers in count:
                count[numbers] += 1
            else: 
                count[numbers] = 1
        
        ordered = sorted(count, key = count.get, reverse = True)

        return ordered[:k]