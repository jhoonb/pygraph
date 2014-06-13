pygraph
=======

Pygraph is the simple library for graph

Class Graph:

- graph.py

- digraph.py

=======

Methods:

- Graph():
    
	- exist_node(node, tp)

	- exist_edge(edge, tp)

	- add_node(node[, weight])

	- add_edge(edge, node_origin, node_destiny[, weight])

	- order()

	- size()

	- update_node_weight(node, weight)

	- update_edge_weight(edge, weight)

	- is_adjacent(node_x, node_y)

	- neighbourhood(node[, neighbourhood_open=True | False])

	- complement()

	- complete()

	- is_complete()

	- del_node(node)

	- del_edge(edge)

	- depth_first_search(node[, debug=True | False]) 

	- load(filename)


- Digraph():

	- exist_node(node, tp)

	- exist_edge(edge, tp)

	- add_node(node[, weight])

	- add_edge(edge, node_origin, node_destiny[, weight])

	- order()

	- size()

	- update_node_weight(node, weight)

	- update_edge_weight(edge, weight)

	- is_adjacent(node_x, node_y)

	- neighbourhood(node[, neighbourhood_open=True])

	- del_node(node)

	- del_edge(edge)

=======


UPDATE
==

File: graph.json (json with configuration for graph) 


Class Graph:

add method: 

- depth_first_search(node[, debug=True | False]) 11/06/2014

- load(filename) 13/06/2014


TODO
==

Class Graph:

- save(filename)


Class Digraph:

- save(filename)

- load(filename)



STATUS = ALPHA ALPHA ALPHA VERSION
==

Sugestions?

jpbanczek@gmail.com
