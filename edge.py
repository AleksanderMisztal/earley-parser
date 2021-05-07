class Edge:
  def __init__(self, head, deps, start, end, hist) -> None:
    self.head = head
    self.deps = deps
    self.start = start
    self.end = end
    self.hist = hist
    
  def getAfterDot(self):
    nt_idx = self.deps.index('*') + 1
    if nt_idx < len(self.deps):
      return self.deps[nt_idx]
    return None

  def __str__(self) -> str:
    return self.head +' -> '+ str(self.deps) +' ['+ str(self.start) +', '+ str(self.end) +'] ' + str(self.hist)

  def hash(self):
    return self.head +' '+ str(self.deps) +' '+ str(self.start) +' '+ str(self.end)

  def __eq__(self, o: object) -> bool:
    return self.hash() == o.hash()
