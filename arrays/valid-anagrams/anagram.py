from collections import defaultdict

def groupAnagrams(strs: list) -> list:
  # defaultdict as list to handle keys which don't exist
  res = defaultdict(list) # maps character count to list of anagrams

  for s in strs:
    count = [0] * 26 # 26 zeros, one for each character
    for c in s:
      # map 'a' to index 0
      # map 'z' to index 25
      
      # ord() gets ascii value 
      # ascii value of a can be 80, b = 81, c = 82 ....
      # 80 - 80 = 0 ('a')
      # 81 - 80 = 1 ('b')
      count[ord(c) - ord("a")] += 1
      
    # group all words with this count together
    # count is a list, and list can't be keys (they are mutable)
    res[tuple(count)].append(s)
  return res.values()

words = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(words))
  