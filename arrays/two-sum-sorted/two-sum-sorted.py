def twoSumSorted(numbers:list,target:int) -> list:
  right_ptr = len(numbers) - 1
  left_ptr = 0
  
  while right_ptr > left_ptr:
    val = numbers[left_ptr] + numbers[right_ptr]
    if val == target:
      return [left_ptr+1,right_ptr+1]
    
    if val > target:
      right_ptr -= 1
    else:
      left_ptr += 1
      
  return [0,0]

arr = [1,2,3,4,5]
target = 9
result = twoSumSorted(arr,target)
print(result)