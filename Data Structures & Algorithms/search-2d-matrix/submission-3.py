class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def middle(start: int, end: int) -> int:
            middle = start + (end - start) // 2
            return middle

        last_values = []

        for sub in matrix:
            last_values.append(sub[-1])
        
        for i in range(len(last_values)):
            if target <= last_values[i]:
                target_row_index = i
                break

        try:
            target_row_list = matrix[target_row_index]
        except:
            return False


        start, end = 0, len(target_row_list) - 1

        while start <= end:
            mid = middle(start, end)
            
            if target_row_list[mid] < target:
                start = mid + 1
            
            elif target_row_list[mid] > target: 
                end = mid - 1

            elif target_row_list[mid] == target:
                return True
        return False      