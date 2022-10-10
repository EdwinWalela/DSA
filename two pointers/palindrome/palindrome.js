function cleanString(str){
  str = str.replace(/[\W+_]/g,'');
  return str.toLowerCase();
}

function isPalindrome(str){
  str = cleanString(str)
  let leftPtr = 0;
  let rightPtr = str.length - 1; 

  while(leftPtr < rightPtr){
    if(str[leftPtr] != str[rightPtr]){
      return false;
    }else{
      leftPtr++;
      rightPtr--;
    }
  }
  return true;
}

console.log(isPalindrome('A man, a plan, a canal: Panama'))