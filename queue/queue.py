class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = ()

  def enqueue(self, item):
    self.storage = (item, *self.storage)
    self.size = len(self.storage)
    pass
  
  def dequeue(self):
    val = None if not self.storage else self.storage[-1]
    self.storage = self.storage[0:-1]
    self.size = len(self.storage)
    return val
    pass

  def len(self):
    return len(self.storage)
    pass
