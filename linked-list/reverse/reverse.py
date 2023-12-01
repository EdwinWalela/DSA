class ListNode:
  def __init__(self,val=0,next=None):
    self.val = val
    self.next = next
    
def revereListIterative(head:ListNode) -> ListNode:
  prev,curr = None, head
  # time = O(n)
  # mem = O(1)
  while curr:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  return prev
