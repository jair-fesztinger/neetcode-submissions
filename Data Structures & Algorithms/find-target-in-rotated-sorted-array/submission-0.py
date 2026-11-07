from collections import deque
class Solution:

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l], l

    
    def search(self, nums: List[int], target: int) -> int:
        value_min, index_min = self.findMin(nums)
        
        if target == value_min:
            return index_min
        elif target >= nums[0] and index_min > 0:
            l, r = 0, index_min - 1
        else:
            l, r = index_min, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1


        return -1