def uniquePaths(m: int, n:int) -> int:
  # bottom row is all 1s
  row = [1] * n
  
  # go through each row except last one
  for i in range(m-1):
    newRow = [1] * n
    
    # n-2 -> go through all rows apart right most (since it will always be 1)
    # -1 -> loop till beginning
    # -1 -> in reverse order 
    for j in range(n - 2, -1, -1):
      # newRow[j+1] -> right 
      # row[j] -> below
      newRow[j] = newRow[j + 1] + row[j]
    # swap prev row with newly calculated row
    row = newRow
  # result will be the first value
  return row[0]


paths = uniquePaths(1,1)
print(paths)