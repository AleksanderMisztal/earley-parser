class Ast:
  def __init__(self, symbol, children) -> None:
    self.symbol = symbol
    self.children = children

  def replaceLeaf(self, idx, tree):
    newChildren = [c for c in self.children]
    newChildren[idx] = tree
    return Ast(self.symbol, newChildren)

  def __str__(self) -> str:
    return '('+str(self.symbol) + ': ' + ', '.join([str(c) for c in self.children]) + ')'
  