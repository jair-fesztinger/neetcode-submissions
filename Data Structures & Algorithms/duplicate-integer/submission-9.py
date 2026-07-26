from collections import deque

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_items = []
        if len(nums) == 0:
            return False
        while len(nums) > 1:
            seen_items.append(nums[0])
            nums.pop(0)
            j = nums[0]

            if j in seen_items:
                return True
        if nums[0] in seen_items:
            return True
        else:
            return False
            