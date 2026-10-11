class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers)-1
        total = numbers[i] + numbers[j]

        while i < j:
            if total == target:
                break
            elif total < target:
                i += 1
                total = numbers[i] + numbers[j]
            elif total > target:
                j -= 1  
                total = numbers[i] + numbers[j]
    
        return [i+1, j+1]        