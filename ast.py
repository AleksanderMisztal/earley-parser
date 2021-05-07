
class Ast:
  def __init__(self, symbol, children) -> None:
      self.symbol = symbol
      self.children = children

  def __str__(self) -> str:
      return self.symbol + ', [' + ', '.join([c.__str__() for c in self.children]) + ']'
  