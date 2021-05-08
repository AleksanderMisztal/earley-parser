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
p = Parser(start, productions)

tests = [
  ['they', 'can', 'fish'],
  ['they', 'can', 'fish', 'in', 'can'],
  ['fish', 'can', 'fish']
]
for t in tests:
  print(' '.join(t))
  asts = p.parse(t)
  for ast in asts:
    print('ast: ', ast)
