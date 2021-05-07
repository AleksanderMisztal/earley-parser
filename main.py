from grammar import Grammar
from earley import Parser

nonterminals = ['S', 'NP', 'VP', 'PP', 'N', 'V', 'P']
terminals = ['can', 'fish', 'they', 'in', 'rivers']
start = 'S'
productions = {
  'S': [['NP', 'VP']],
  'NP': [['N', 'PP'], ['N']],
  'PP': [['P', 'NP']],
  'VP': [['VP', 'PP'], ['V', 'VP'], ['V', 'NP'], ['V']]
}
termProds = {
  'N': [['can'], ['fish'], ['rivers']],
  'P': [['in']],
  'V': [['can'], ['fish']]
}

g = Grammar(nonterminals, terminals, start, productions, termProds)

ast = Parser(g).parse(['they', 'can', 'fish'])
#print(ast)