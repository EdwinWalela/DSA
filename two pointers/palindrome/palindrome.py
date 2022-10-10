import re


def is_palindrome(str):
  def clean_string(str):
    str = str.lower()
    return re.sub(r'\W+','',str)
  
  str = clean_string(str)
  leftPtr = 0
  rightPtr = len(str) - 1
  
  while leftPtr < rightPtr:
    if str[leftPtr] != str[rightPtr]:
      return False
    else:
      leftPtr = leftPtr + 1
      rightPtr = rightPtr - 1
  return True

print(is_palindrome('A man, a plan, a canal: Panama'))