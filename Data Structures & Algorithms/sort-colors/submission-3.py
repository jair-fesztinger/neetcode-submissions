class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = [0] * (max(nums)+1) 
        for i in nums:
            count[i] += 1

        k = 0
        for j in range(len(count)):
            while count[j] > 0:
                nums[k] = j
                count[j] -= 1
                k += 1     

    

    #how do we assign indexes that default to zero