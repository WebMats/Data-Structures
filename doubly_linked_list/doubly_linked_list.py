"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    # if not not next:
    #   print('HERE', next.value)
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.length == 0:
      self.tail = ListNode(value)
      self.head = ListNode(value)
      self.length = 1 
    else:
      self.head = ListNode(value, next=self.head)
      self.head.next.prev = self.head
      self.length += 1
    pass

  def remove_from_head(self):
    past_head = self.head
    if self.length == 1:
      self.tail = None
      self.head = None
      self.length = 0 
    else:
      self.head = None
      self.length -= 1
    return past_head.value
    pass

  def add_to_tail(self, value):
    if self.length == 0:
      self.tail = ListNode(value)
      self.head = ListNode(value)
      self.length = 1 
    else:
      self.tail = ListNode(value, self.tail)
      self.tail.prev.next = self.tail
      self.length += 1
    pass

  def remove_from_tail(self):
    past_tail = self.tail
    if self.length == 1:
      self.tail = None
      self.head = None
      self.length = 0 
    else:
      self.head = None
      self.length -= 1
    return past_tail.value
    pass

  def move_to_front(self, node):
    if self.length == 0 or self.length == 1:
      print('end')
    else:
      if node == self.tail:
        self.tail = node.prev
      else:  
        hold = node.prev
        node.prev.next = node.next
        node.next.prev = hold
      hold_head = self.head
      self.head = node
      hold_head.prev = node
      self.head.next = hold_head
    pass

  def move_to_end(self, node):
    if self.length == 0 or self.length == 1:
      print('end')
    else:
      if node == self.head:
        self.head = node.next
      else:  
        hold = node.prev
        node.prev.next = node.next
        node.next.prev = hold
      hold_tail = self.tail
      self.tail = node
      hold_tail.next = node
      self.tail.prev = hold_tail
    pass

  def delete(self, node):
    if self.length == 1:
      self.head = None
      self.tail = None
    elif self.length == 2:
      self.head = self.tail
    else:
      if self.head == node:
        self.head = self.head.next
      elif self.tail == node:
        self.tail = node.prev
      else:
        hold_prev = node.prev
        node.prev.next = node.next
        node.next.prev = hold_prev
    self.length -= 1
    pass
    
  def get_max(self):
    pass
