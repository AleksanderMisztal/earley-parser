from edge import Edge
from east import Ast

def isNonterminal(token: str):
  return token == token.upper()

class Parser:
  def __init__(self, start, prods):
      self.start = start
      self.prods = prods
      self.edges: list[list[Edge]] = None
  
  def parse(self, words: 'list[str]'):
    self.initParse(len(words))
    for k, word in enumerate(words + ['END']):
      #print(word)
      it = 0
      while it < len(self.edges[k]):
        e = self.edges[k][it]
        dot_idx = e.deps.index('*')
        if dot_idx+1 < len(e.deps):
          # no more tokens, should only complete
          if k == len(words): 
            it+= 1
            continue
          token = e.deps[dot_idx+1]
          if isNonterminal(token):
            for prod in self.prods[token]:
              self.addEdge(k, Edge(token, ['*']+prod, k, Ast(token, prod)))
          else:
            if token == word and token in [ts[0] for ts in self.prods[e.head]]:
              self.addEdge(k+1, Edge(e.head, [token, '*'], e.start, Ast(e.head, [token])))
        else:
          for oe in self.edges[e.start]:
            if oe.getAfterDot() == e.head:
              newDeps = [d for d in oe.deps]
              idx = newDeps.index('*')
              newDeps[idx] = newDeps[idx+1]
              newDeps[idx+1] = '*'
              ne = Edge(oe.head, newDeps, oe.start, oe.ast.replaceLeaf(idx, e.ast))
              self.addEdge(k, ne)
              if ne.start == 0 and k == len(words):
                yield ne.ast
        it+=1
  
  def initParse(self, length):
    self.edges = [[] for _ in range(length+1)]
    s = self.start
    sProds = self.prods[s][0]
    self.addEdge(0, Edge(s, ['*']+sProds, 0, Ast(s, sProds)))

  def addEdge(self, k, edge):
    if edge not in self.edges[k]:
      self.edges[k].append(edge)
      #print(len(self.edges[k])-1, ' ', edge)
