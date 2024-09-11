# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class StackMin:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.min_stack: list[int] = []
    
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    
    def pop(self) -> int:
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
    
    def min(self) -> int | None:
        if not self.min_stack:
            return None
        return self.min_stack[-1]

