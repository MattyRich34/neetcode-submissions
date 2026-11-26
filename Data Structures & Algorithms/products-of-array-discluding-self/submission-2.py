class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n                # [1, 1, 1, 1], one slot per position

        # Pass 1: left to right, store left products
        left = 1                        # nothing to the left of the first spot
        for i in range(n):
            answer[i] = left            # everything before i
            left *= nums[i]             # include nums[i] for the NEXT spot
        # answer is now [1, 1, 2, 6]

        # Pass 2: right to left, multiply in right products
        right = 1                       # nothing to the right of the last spot
        for i in range(n - 1, -1, -1):  # i = 3, 2, 1, 0 (backwards)
            answer[i] *= right          # left product × everything after i
            right *= nums[i]            # include nums[i] for the NEXT spot (to the left)
        # answer is now [24, 12, 8, 6]

        return answer