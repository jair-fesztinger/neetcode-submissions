import heapq
class MinStack:

    def __init__(self):
        self.stack = [] #initialize stack per object
        self.mini = [] #track minimum value for O(1) access

    def push(self, val: int) -> None:
        if not self.stack:
            self.mini.append(val)

        elif self.stack:
            if self.mini[-1] >= val:
                self.mini.append(val)
        
        return self.stack.append(val)
        

    def pop(self) -> None:
    
        if not self.mini:
            return 
        else:
            pop_value = self.stack.pop()
            if pop_value == self.mini[-1]:
                self.mini.pop()
        return pop_value
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int: 
        if not self.stack:
            return 

        return self.mini[-1]