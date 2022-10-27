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


print(two_sum_brute([1,2,3,4],3))

