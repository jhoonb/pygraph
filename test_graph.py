# -----------------------------------------------------
# test_graph.py
# Author: Jhonathan Paulo Banczek.
# jhoob.com - jpbanczek@gmail.com
# Python 3 >
#------------------------------------------------------

from graph import Graph
from graph import Digraph

g = Graph(name='Grafo G')

print("add vertices")
g.add_node(['1','2','3','4', '5', '6', '7', '8', '9','10','11','12','13', 14])


print("add edges")
for i in range(2,15):
    g.add_edge(None, str(1), str(i), 0)

print('\ngrafo complemento...')
gc = g.complement()
gc.show()

print('\ngrafo completo...')
gcc = g.complete()
gcc.show()