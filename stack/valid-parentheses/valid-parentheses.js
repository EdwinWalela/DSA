function isValid(str){
  let stack = [];
  let closeToOpen = new Map();

  closeToOpen.set(']','[')
  closeToOpen.set(')','(')
  closeToOpen.set('}','{')

  for(let i = 0; i < str.length; i++){
    if(closeToOpen.has(str[i])){
      if(
          stack.length>0 
          &&
          stack[stack.length-1] == closeToOpen.get(str[i])){
        stack.pop();
      }else{
        return false;
      }
    }else{
      stack.push(str[i]);
    }
  }
  return stack.length == 0
}

console.log(isValid('(())'))