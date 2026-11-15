class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}

        for num in nums:
            if num in store:
                store[num] += 1 
            else: 
                store[num] = 1
        organized = sorted(store, key = store.get, reverse = True)
        return organized[:k]