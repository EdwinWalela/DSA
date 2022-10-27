from re import I


def two_sum_brute(arr:list,target:int) -> list:
  i = 0
  while i < len(arr):
    k = i + 1
    while k < len(arr):
      if arr[i] + arr[k] == target:
        return [i,k]
      k = k + 1
    i = i + 1
  return [0,0]

def two_sum(arr:list,target:int) ->list:
  arr_map = {}
  
  for idx,num in enumerate(arr):
    diff = target - num
    
    if diff not in arr_map:
      arr_map[num] = idx
    else:
      return [arr_map[diff],idx]
  
  return [0,0]

print(two_sum([1,2,3,4,5,6,7],13))

