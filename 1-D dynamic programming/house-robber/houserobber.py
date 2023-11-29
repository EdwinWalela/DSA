def rob(nums):
  rob1, rob2 = 0 , 0
  
  # [rob1, rob2, n, n+1, ......]
  # [ 1,    2,   3, 1    ]
  for n in nums:
    print(f'rob1={rob1} rob2={rob2}')
    temp = max(n + rob1, rob2)
    print(temp)
    rob1 = rob2
    rob2 = temp
  return rob2

nums = [1,2,3,1]
print(rob(nums))