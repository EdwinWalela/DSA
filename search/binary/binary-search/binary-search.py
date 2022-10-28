def binary_search(arr:list,target:int)->int:
  left_prt = 0
  right_ptr = len(arr) -1
  
  while left_prt <= right_ptr:
    mid = (left_prt + right_ptr) // 2
    
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left_prt = mid + 1
    elif arr[mid] > target:
      right_ptr = mid - 1
  
  return -1

arr = [-1,0,3,5,9,12]
target = 9

print(binary_search(arr,target))