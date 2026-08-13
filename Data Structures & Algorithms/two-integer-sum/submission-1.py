class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        for i in range(len(nums)):

            j = len(nums) - 1
            while j > 0:
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    j -= 1

