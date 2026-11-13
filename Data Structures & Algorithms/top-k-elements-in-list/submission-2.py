class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        for number in nums: 
            if number in check:
                check[number] += 1
            else: 
                check[number] = 1
        answer = sorted(check, key = check.get, reverse = True)
        
        return answer[:k]