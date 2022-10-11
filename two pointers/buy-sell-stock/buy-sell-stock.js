function maxProfit(days){
  let maxProfit = 0;
  let leftPrt = 0;
  let rightPtr = 1;

  while(rightPtr<days.length-1){
    let profit = days[rightPtr] - days[leftPrt];
  
    if(profit>0){
      if(profit>maxProfit){
        maxProfit = profit;
      }
      rightPtr++;
    }else{
      leftPrt = rightPtr;
      rightPtr++;
    }
  }
  return maxProfit;
}

console.log(maxProfit([7,1,5,3,6,4]))