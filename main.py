from east import Ast
from earley import Parser

start = 'S'
productions = {
  'S': [['NP', 'VP']],
  'NP': [['N', 'PP'], ['N']],
  'PP': [['P', 'NP']],
  'VP': [['VP', 'PP'], ['V', 'VP'], ['V', 'NP'], ['V']],
  'N': [['they'],['can'], ['fish'], ['rivers']],
  'P': [['in']],
  'V': [['can'], ['fish']]
}

asts = Parser(start, productions).parse(['they', 'can', 'fish'])
for ast in asts:
  print('ast: ', ast)
