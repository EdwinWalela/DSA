import collections
from typing import List


def numIslands(grid:List[List[str]])->int:
  if not grid:
    return 0
  
  # Get grid dimensions
  rows, cols = len(grid), len(grid[0])
  visit = set()
  islands = 0
  
  def bfs(r,c):
    q = collections.deque()
    visit.add((r,c))
    q.append((r,c))
    
    while q:
      row,col = q.popleft()
      directions = [[1,0],[-1,0],[0,1],[0,-1]]
      
      # Check adjacent nodes (top,bottom,right,left)
      for dr,dc in directions:
        r = row + dr
        c = col + dc        
       
        if(
            r in range(rows) and  # Check if row is within bounds of our grid
            c in range(cols) and  # Check if col is within bounds of our grid
            grid[r][c] == "1" and # Check if current value is land
            (r ,c) not in visit   # Check if current value hasn't been visited
          ):
          q.append((r,c))
          visit.add((r,c))
   
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == "1" and (r,c) not in visit:
        bfs(r,c)
        islands += 1
  return islands



grid = [
 ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
result = numIslands(grid)
print(result)