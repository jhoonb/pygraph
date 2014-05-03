# -----------------------------------------------------
# test_graph.py
# Author: Jhonathan Paulo Banczek.
# jhoob.com - jpbanczek@gmail.com
# Python 3 >
#------------------------------------------------------

from graph import Graph

g = Graph(id='Grafo G')

#print(g)

#g.show()

g.add_node(['1', '2', '3', '4'])

g.add_edge(None, '1', '2')# -> ('12', '1', '2')
g.add_edge(None, '2', '3')
g.add_edge(None, '4', '1')
g.add_edge(None, '4', '3')
g.add_edge(None, '4', '2')
g.add_edge(None, '1', '3')

g.show()
"""print(g.size())
print(g.order())

print('grafo simples:')
print('1-4: True ->' ,g.is_adjacent('1','4'))
print('1-2: True ->' ,g.is_adjacent('1','2'))
print('1-3: False ->' ,g.is_adjacent('1','3'))
print('4-1: True ->' ,g.is_adjacent('4','1'))
print('3-1: False ->' ,g.is_adjacent('3','1'))

print('vizinhança(aberta): 1 -> ', g.neighbourhood('1'))
print('vizinhança(fechada): 1 -> ', g.neighbourhood('1', False))

print('-------------------------')
g._digraph = True

print('digrafo: ')
print('1-4: False ->' ,g.is_adjacent('1','4'))
print('1-2: True ->' ,g.is_adjacent('1','2'))
print('1-3: False ->' ,g.is_adjacent('1','3'))
print('4-1: True ->' ,g.is_adjacent('4','1'))
print('3-1: False ->' ,g.is_adjacent('3','1'))
print('vizinhança(aberta): 1 -> ', g.neighbourhood('1'))
print('vizinhança(fechada): 1 -> ', g.neighbourhood('1', False))
"""

gl = g.complement()
g.is_complete()
