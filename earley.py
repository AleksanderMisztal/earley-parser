from ast import Ast
from grammar import Grammar
from edge import Edge

class Parser:
  dot = '*'
  
  def __init__(self, grammar: Grammar):
      self.g = grammar
      self.edges: list[Edge] = []

  def parse(self, tokens: 'list[str]'):
    g = self.g
    self.edges = []
    self.edges.append(Edge(g.start, [self.dot]+g.productions[g.start][0], 0, 0, []))
    self.predict(0)
    print('\n'.join([e.__str__() for e in self.edges]))
    return Ast('X',[])
  
  def predict(self, begin):
    it = begin
    while it < len(self.edges):
      e = self.edges[it]
      it+=1
      nt_idx = e.deps.index(self.dot) + 1
      if nt_idx == len(e.deps): continue
      nt = e.deps[nt_idx]
      if nt not in self.g.productions: continue
      for prod in self.g.productions[nt]:
        newEdge = Edge(nt, [self.dot]+prod, e.end, e.end, [])
        if newEdge not in self.edges:
          self.edges.append(newEdge)
  
  def scan(self, begin):
    it = begin
    while it < len(self.edges):
      e = self.edges[it]
      it+=1
      nt_idx = e.deps.index(self.dot) + 1
      if nt_idx == len(e.deps): continue
      nt = e.deps[nt_idx]
      if nt not in self.g.productions: continue
      if  in self.g.termProds[nt]:
        newEdge = Edge(nt, nt+[self.dot], e.end, e.end, [])
        if newEdge not in self.edges:
          self.edges.append(newEdge)
  
    

