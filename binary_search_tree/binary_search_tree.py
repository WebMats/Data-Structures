class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    pass

  def contains(self, target):
    if self.value == target:
      return True
    elif target < self.value and not self.left == None:
      return self.left.contains(target)
    elif target >= self.value and not self.right == None:
      return self.right.contains(target)
    else:
      return False
    pass

  def get_max(self):
    if self.right == None:
      return self.value
    else:
      return self.right.get_max()
    pass

  def for_each(self, cb):
    cb(self.value)
    if not self.left == None:
      self.left.for_each(cb)
    if not self.right == None:
      self.right.for_each(cb)
    pass