class Edge:
  def __init__(self, head, deps, start, end, hist) -> None:
      self.head = head
      self.deps = deps
      self.start = start
      self.end = end
      self.hist = hist

  def __str__(self) -> str:
      return self.head +' -> '+ str(self.deps) +' ['+ str(self.start) +', '+ str(self.end) +'] ' + str(self.hist)
  
  def __eq__(self, o: object) -> bool:
      return str(self) == str(o)
