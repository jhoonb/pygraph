# -----------------------------------------------------
# test_graph.py
# Author: Jhonathan Paulo Banczek.
# jhoob.com - jpbanczek@gmail.com
# Python 3 >
#------------------------------------------------------

from graph import Graph
from graph import Digraph

g = Graph(name='Grafo G')

g.add_node([1,2,3])

g.add_edge(None, 1, 2)

g.add_edge(None, 1, 3)

g.add_edge(None, 2, 3)

print(g.is_complete())

g.del_edge('13')

print(g.is_complete())

g.add_edge(None, 3, 3)

print(g.is_complete())

g.del_edge('33')

g.add_edge(None, 1, 3)

print(g.is_complete())