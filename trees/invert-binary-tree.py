from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def invertTree(root):
  if not root:
    return None
  # swap children
  root.left, root.right = root.right, root.left
  
  invertTree(root.left)
  invertTree(root.right)
  
  return root
  