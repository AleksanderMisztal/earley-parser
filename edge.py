class Edge:
  def __init__(self, head, deps, start, ast) -> None:
    self.head: str = head
    self.deps: list[str] = deps
    self.start: int = start
    self.ast = ast
    
  def getAfterDot(self) -> str:
    nt_idx = self.deps.index('*') + 1
    if nt_idx < len(self.deps):
      return self.deps[nt_idx]
    return None

  def __str__(self) -> str:
    return self.head +' -> '+ str(self.deps) +' '+ str(self.start)+' Ast(' + str(self.ast)+')'

  def hash(self):
    return self.head +' '+ str(self.deps) +' '+ str(self.start)

  def __eq__(self, o: object) -> bool:
    return self.hash() == o.hash()
