def contains_duplicate(nums):
  hash_map = dict({})
  
  for num in nums:
    curr_val = hash_map.get(num)
    if curr_val is None:
      hash_map[num] = 1
    else:
      return True
  
  return False

nums = [1,2,3,4,1]

print(contains_duplicate(nums))