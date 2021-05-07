from grammar import Grammar
from edge import Edge

def isNonterminal(token: str):
  return token == token.upper()

class Parser:
  dot = '*'
  
  def __init__(self, grammar: Grammar):
      self.g = grammar
      self.edges: list[Edge] = []

  def addEdge(self, edge):
    if edge not in self.edges:
      self.edges.append(edge)
      print(len(self.edges)-1, ' ', edge)
  
  def parse(self, words: 'list[str]'):
    self.addEdge(Edge(self.g.start, [self.dot]+self.g.productions[self.g.start][0], 0, 0, []))
    for word in words:
      print(word)
      it = 0
      while it < len(self.edges):
        e = self.edges[it]
        et_idx = e.deps.index(self.dot) + 1
        if et_idx < len(e.deps):
          token = e.deps[et_idx]
          if isNonterminal(token):
            for prod in self.g.productions[token]:
              self.addEdge(Edge(token, [self.dot]+prod, e.end, e.end, [it,'predict']))
          else:
            if token == word and token in [ts[0] for ts in self.g.productions[e.head]]:
              self.addEdge(Edge(e.head, [token, self.dot], e.start, e.end+1, [it, 'scan']))
        else:
          for oe in self.edges:
            if oe.getAfterDot() == e.head:
              newDeps = [d for d in oe.deps]
              idx = newDeps.index(self.dot)
              newDeps[idx] = newDeps[idx+1]
              newDeps[idx+1] = self.dot
              self.addEdge(Edge(oe.head, newDeps, oe.start, e.end, [it,'complete']))
          break
        it+=1
  
    

