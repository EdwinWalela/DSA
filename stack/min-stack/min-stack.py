class MinStack:

    def __init__(self):
      self.stack = []
      self.minStack = []

    def push(self, val: int) -> None:
      self.stack.append(val)
      if self.minStack:
        val = min(val,self.minStack[-1])
      self.minStack.append(val)
      
    def pop(self) -> None:
      self.stack.pop()
      self.minStack.pop()

    def top(self) -> int:
      return self.stack[-1]

    def getMin(self) -> int:
      return self.minStack[-1]

obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(f"top = {param_3}")
print(f"min = {param_4}")