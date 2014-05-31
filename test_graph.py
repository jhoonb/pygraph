# -----------------------------------------------------
# test_graph.py
# Author: Jhonathan Paulo Banczek.
# jhoob.com - jpbanczek@gmail.com
# Python 3 >
#------------------------------------------------------

from graph import Graph

g = Graph(id='Grafo G')

print("add vertices")
g.add_node(['1', '2', '3', '4', '5'])


print("add edges")
g.add_edge(None, '1', '2')
g.add_edge(None, '1', '4')
g.add_edge(None, '3', '5')
g.add_edge(None, '4', '5')
g.add_edge(None, '5', '2')

g.show()
print("*" * 68)

gl = g.complement()

gl.show()
print("*" * 68)

gc = g.complete()
gc.show()
print("*" * 68)
