from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count1 = 0
        while students and sandwiches:
            k = len(students)

            if k == count1:
                break
            

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count1 = 0
            else:
                students.append(students.pop(0))
                count1 += 1
        return len(students)
    
