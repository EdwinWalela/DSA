import heapq

class KthLargest:
  def __init__(self,k:int,nums):
    self.minHeap = nums
    self.k = k
    heapq.heapify(self.minHeap)
    while len(self.minHeap) > self.k:
      heapq.heappop(self.minHeap)
    
  def add(self,val:int) -> int:
    heapq.heappush(self.minHeap,val)
    # only pop if there are more than k items in the minheap
    if len(self.minHeap) > self.k:
      heapq.heappop(self.minHeap)
    return self.minHeap[0]
    
k = 3
nums = [4,5,8,2]
obj = KthLargest(k,nums)

larg1 = obj.add(3)
larg2 = obj.add(5)
larg3 = obj.add(10)
larg4 = obj.add(9)
larg5 = obj.add(4)

print(larg1)
print(larg2)
print(larg3)
print(larg4)
print(larg5)