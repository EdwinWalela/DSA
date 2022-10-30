def longest_length_substr(s:str)->int:
  charSet = set()
  left_prt = 0
  max_length = 0
  
  for right_ptr in range(len(s)):
    while s[right_ptr] in charSet:
      charSet.remove(s[left_prt])
      left_prt += 1
    charSet.add(s[right_ptr])
    max_length = max(max_length,len(charSet))

  return max_length


res = longest_length_substr("abcde")
print(res)