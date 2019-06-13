class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage) - 1
    self._bubble_up(index)
    pass

  def delete(self):
    top = self.storage[0]
    if len(self.storage) == 1:
      self.storage = []
      return top
    self.storage = [self.storage[-1], *self.storage[1: -1]]
    self._sift_down(0)
    return top
    pass

  def get_max(self):
    return self.storage[0]
    pass

  def get_size(self):
    return len(self.storage)
    pass

  def _bubble_up(self, index):
    while index > 0:
      parent = (index-1) // 2
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
      else:
        break
    pass

  def _sift_down(self, index):
    if len(self.storage) < 2:
      return 
    left_i = 2 * index + 1
    right_i = left_i + 1
    next_i = None
    if len(self.storage) - 1 >= right_i and self.storage[right_i] > self.storage[index] and self.storage[right_i] > self.storage[left_i]:
      self.storage[right_i], self.storage[index] = self.storage[index], self.storage[right_i]
      next_i = right_i
    elif len(self.storage) - 1 >= left_i and self.storage[left_i] > self.storage[index]:
      self.storage[left_i], self.storage[index] = self.storage[index], self.storage[left_i]
      next_i = left_i
    else:
      return
    next_i = left_i if not next_i else next_i
    self._sift_down(next_i)
    pass



#get left child: 2 * index + 1
#get right child: 2 * index + 2
#get parent: (index - 1 )// 2
