def maxProfit(prices:list)->int:
  left_prt = 0
  right_prt = 1
  max_profit = 0
  
  while right_prt < len(prices):
    profit = prices[right_prt] - prices[left_prt]
    
    if profit > 0:
      max_profit = max(profit,max_profit)
      right_prt += 1
    else:
      left_prt = right_prt
      right_prt += 1
  
  return max_profit

prices = [7,1,5,3,6,4]
res = maxProfit(prices)
print(res)