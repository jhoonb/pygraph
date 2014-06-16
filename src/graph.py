'''
@package graph.py
@author Jhonathan Paulo Banczek
@date 2014
jpbanczek@gmail.com -- jhoonb.com
'''

#not uncomment this!
#ANSWER_TO_THE_ULTIMATE_QUESTION_OF_LIFE_THE UNIVERSE_AND_EVERYTHING = 42

from itertools import combinations
import json

'''
@brief define errors
'''
_error_ = { 0: 'Error [0]: There is already a node in the graph',
           1: 'Error [1]: Length nodes and length weight not equal',
           2: 'Error [2]: This edge exists in the graph',
           3: 'Error [3]: There is no such node in the graph',
           4: 'Error [4]: w is not a valid value',
           5: 'Error [5]: Not a weighted graph',
           7: 'Error [7]: No such edge exists in the graph',
           8: 'Error [8]: Only simple graph',
           9: 'Error [9]: Only the value of the node type str'
}

class Graph(object):
    '''
    @brief class Graph
    -----------
    attributes:
    -----------
    - _graph_id: (str)
    - _typegraph: (str)-> graph, digraph
    - weighted: (bool)->True, False
    - _node: (dict)
        _node = { 'node_id': [ weight, [] } where [] is adjacency list
    - _edge: (dict)
        _edge = {'edge_id': [[node_origin, node_destiny, weight]] }
    --------
    methods:
    --------
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
    - complement()
    - complete()
    - is_complete()
    - del_node(node)
    - del_edge(edge)
    - line_graph()
    '''

    def __init__(self, graph_id='Graph', weighted=False):
        '''
        @param graph_id (str): id of graph
        @param weighted (bool): if graph is weighted
        '''

        self._graph_id = graph_id
        self._typegraph = 'graph'
        self.weighted = weighted
        self._node = {}
        self._edge = {}


    def exist_node(self, node, tp='any'):
        '''
        @brief Check if node(s) exist in graph
        @param node (str | list): node
        @param tp (str): 'any' | 'all' (default: any)
        @return (bool)
        '''

        if isinstance(node, list):
            if tp is 'any':
                if any([i in self._node for i in node]):
                    return True
            else:
                if all([i in self._node for i in node]):
                    return True
        else:
            if node in self._node:
                return True

        return False


    def exist_edge(self, edge, tp='any'):
        '''
        @brief Check if edge(s) exist in graph
        @param edge (str | list): edge
        @param tp (str): 'any' | 'all' (default: any)
        @return (bool)
        '''

        if isinstance(edge, list):

            if tp is 'any':
                if any([i in self._edge for i in edge]):
                    return True
            else:
                if all([i in self._edge for i in edge]):
                    return True
        else:
            if edge in self._edge:
                return True

        return False


    def add_node(self, node, weight=[0]):
        '''
        @brief add node(s) in the graphs
        @param node (str | list): node
        @param weighted (list): weighted of the nodes
        is optional
        '''

        # only str type
        if isinstance(node, (int, float)):
            node = str(node)
        elif isinstance(node, list):
            node = [str(i) for i in node]
        else:
            raise Exception(_error_[9])

        #check if exist node in graph
        if self.exist_node(node):
            raise Exception(_error_[0])

        if not self.weighted:
            weight = [0 for i in node]

        #check if all elements of weight is int or float type
        check = all([isinstance(i, (int, float)) for i in weight])

        if len(node) == len(weight) and check:
            for i in range(len(node)):
                self._node[node[i]] = [weight[i], []]
        else:
            raise Exception(_error_[1])


    def add_edge(self, edge, node_origin, node_destiny, weight=0):
        '''
        @brief add edge in graph
        @param edge (str): id of edge
        @param node_origin (str)
        @param node_destiny (str)
        @param weight (float | int): weight of the edge
        '''

        # only str type
        node_origin = str(node_origin)
        node_destiny = str(node_destiny)

        # create id edge if None
        if edge is None:
            edge = node_origin + node_destiny

        # check if edge exist in graph
        if self.exist_edge(edge):
            raise Exception(_error_[2])
        
        # Only graph
        if self._typegraph is 'graph':
            if self.is_adjacent(node_origin, node_destiny) is True \
            or self.is_adjacent(node_destiny, node_origin) is True:
                raise Exception(_error_[2])
                

        # check if nodes not exist in graph
        if not self.exist_node([node_origin, node_destiny], 'all'):
            raise Exception(_error_[3])

        # check weight type, only int or float
        if isinstance(weight, (int, float)):
            self._edge[edge] = [node_origin, node_destiny, weight]
            # insert adjacency list
            self._node[node_origin][1].append(node_destiny)
            # insert if digraph object
            if self._typegraph is not 'digraph':
                self._node[node_destiny][1].append(node_origin)
        else:
            raise Exception(_error_[4])
            

    def order(self):
        '''
        @brief cardinality of the set of nodes
        @return (int)
        '''
        return len(self._node)


    def size(self):
        '''
        @brief cardinality of the set of edges
        @return (int)
        '''
        return len(self._edge)


    def update_node_weight(self, node, weight):
        '''
        @brief update the weight of the node
        @param node (str)
        @param weight (int | float)
        '''

        # only str
        node = str(node)

        if not self.exist_node(node):
            raise Exception(_error_[3])

        if not isinstance(w, (int, float)):
            raise Exception(_error_[4])

        self._node[node][1] = weight


    def update_edge_weight(self, edge, weight):
        '''
        @brief update weighted of edge
        @param edge (str)
        @param weight (int | float)
        '''

        # only str
        edge = str(edge)

        # check if nodes not exist in graph
        if not self.exist_node(edge):
            raise Exception(_error_[7])

        # check weight type, only int or float
        if not isinstance(weight, (int, float)):
            raise Exception(_error_[4])

        #update weight
        self._edge[edge][2] = weight


    def is_adjacent(self, node_x, node_y):
        '''
        @brief check if node_x is adjacent to node_y
        @param node_x (str)
        @param node_y (str)
        @return (bool)
        '''

        #only str
        node_x = str(node_x)
        node_y = str(node_y)

        #check if nodes no exist in the graph
        if not self.exist_node([node_x, node_y], 'all'):
            raise Exception(_error_[3])

        if node_y in self._node[node_x][1] or node_x in self._node[node_y][1]:
            return True

        return False


    def neighbourhood(self, node, neighbourhood_open=True):
        '''
        @brief neighbourhood of the node in the graph
        @param node (str)
        @param neighbourhood_open (bool): default (True)
        @return (list)
        '''

        # only str
        node = str(node)

        # check if node not exist in the graph
        if not self.exist_node(node):
            raise Exception(_error_[3])

        output = [i for i in self._node if self.is_adjacent(i, node)]

        if neighbourhood_open:
            return output
        else:
            output.insert(0, node)
            return output


    def complement(self):
        '''
        @brief Generate graph complement of the graph
        @return (Graph)
        '''
        
        if self._typegraph is not 'graph':
            raise Exception(_error_[8])
            
        # set nodes
        nodes = [i for i in self._node]
        # set edges of graph
        edges = [tuple((self._edge[i][:2])) for i in self._edge]
        # all combinations of edges
        all_edges = list(combinations(nodes, 2))
        # remove is loop
        all_edges = [i for i in all_edges if not i[0] == i[1]]
        # remove edges
        all_edges = [i for i in all_edges if i not in edges]
        # remove edges reverse
        all_edges = [i for i in all_edges if (i[1], i[0]) not in edges]
        # create a new object Graph()
        gc = Graph(graph_id='Complement of ' + self._graph_id)

        # add the nodes
        gc.add_node(nodes)

        # add the edges
        for i in all_edges:
            gc.add_edge(None, i[0], i[1])

        return gc


    def complete(self):
        '''
        @brief Generate graph complete of the graph
        @return (Graph)
        '''
        
        if self._typegraph is not 'graph':
            raise Exception(_error_[8])

        # set nodes
        nodes = [i for i in self._node]
        # all combinations of edges
        all_edges = list(combinations(nodes, 2))
        # remove is loop
        all_edges = [i for i in all_edges if not i[0] == i[1]]
        # create graph object
        g_complete = Graph(graph_id="Complete")
        # add nodes
        g_complete.add_node(nodes)

        for i in all_edges:
            g_complete.add_edge(None, i[0], i[1])

        return g_complete

    
    def is_complete(self):
        '''
        @brief Check if graph is complete
        @return (bool)
        '''
        
        if self._typegraph is not 'graph':
            raise Exception(_error_[8])

        # set edges
        edges = [tuple(self._edge[i][:2]) for i in self._edge]
        # all combinations of edges
        all_edges = list(combinations([i for i in self._node], 2))
        # remove is loop
        all_edges = [i for i in all_edges if not i[0] == i[1]]
        # get length of set
        check = len([i for i in all_edges
                 if i not in edges and (i[1], i[0]) not in edges])

        if check == 0:
            return True
        
        return False


    def del_node(self, node):
        '''
        @brief Delete node from graph
        @param node (str)
        '''

        # only str
        node = str(node)
        # check if not exist node in graph
        if not self.exist_node(node):
            raise Exception(_error_[3])

        # set edges delete
        edges = [i for i in self._edge if node in self._edge[i][:2]]
        # delete edges
        for i in edges:
            self._edge.pop(i)
            
        _check = lambda x, y: x in self._node[y][1]
        
        # delete nodes of adjacency list
        for i in self._node:
            if _check(node, i):
                self._node[i][1].remove(node)
                
        # delete node
        del self._node[node]

        
    def del_edge(self, edge):
        '''
        @brief delete edge of graph
        @param node (str)
        '''

        # only str
        edge = str(edge)
        # check if node not exist in graph
        if not self.exist_edge(edge):
            raise Exception(_error_[7])

        # set nodes
        node_x, node_y = self._edge[edge][:2]

        _check = lambda x, y: x in self._node[y][1]
        # delete node node_x of adjacency list
        # delete node node_y of adjacency list
        for i in self._node:
            if _check(node_x, i):
                self._node[i][1].remove(node_x)
            if _check(node_y, i):
                self._node[i][1].remove(node_y)

        # delete edge
        del self._edge[edge]


    def dijkstra(self, x, w):
        '''
        @brief
        @param
        @param
        @return
        '''
        """
        Algoritmo de Dijkstra para o menor caminho em um grafo.
        O Grafo tem que ser ponderado (conter pesos) e não pode ter
        pesos negativos.
        """
        pass


    def depth_first_search(self, node_x, debug=False):
        '''
        @brief depth-first search
        @param node_x (str)
        @param debug (bool)
        '''
        
        def _dfs(v):
            
            if debug:
                print('\t-> Exploring: ', v)
            
            for w in self._node[v][1]:
                if nd[w] is False:
                    nd[w] = True
                    if debug:
                        print('-> Node: ', w, ' | visited')
                    _dfs(w)
        
        # dict[nodes] = status visited (bool)
        nd = {}
        
        # all False (visited)
        for i in self._node:
            nd[i] = False 
        
        # visited node_x
        nd[node_x] = True
        
        if debug:
            print('-> Node: ', node_x, ' | visited')
            
        #explore dfs v
        _dfs(node_x)
        

    def bfs(self, node_x):
        '''
        @brief breadth-first search
        @param
        @param
        @return
        '''
        pass


    def line_graph(self):
        '''
        @brief line graph L(G) -> G | complexity: O(n²)
        @return (Graph)
        '''
        
        gl = Graph(graph_id="L({})".format(self._graph_id))
        
        # create nodes
        # nodes in V(L(G)) = E(G)
        gl.add_node([i for i in self._edge])
        
        # E(L(V))
        gl_edges = []
        
        # e and j element of E(G)
        # x and y is nodes from extreme edes e
        # condition: check if x and y exist in set E(G) AND
        # [e, j] and [j, e] edges not in E(L(G))
        for e in self._edge:
            x, y = self._edge[e][:2]
            for j in self._edge:
                if j != e:
                    if (x in self._edge[j][:2] \
                    or y in self._edge[j][:2]) \
                    and ([e, j] not in gl_edges and [j, e] not in gl_edges):
                        gl_edges.append([e, j])
                        
        # add edges in gl -> E(L(G))
        for i in gl_edges:
            gl.add_edge(None, i[0], i[1])
                                
        return gl
    
    
    def load(self, filename):
        '''
        @brief load configuration in .json
        @param filename (str): name file
        '''
        
        try:
            fl = open(filename, 'r')
            fl_graph = json.load(fl)
            fl.close()
        except:
            raise Exception('Error in file read/write.')
        
        # check types
        tps = ['graph', 'digraph']
        if fl_graph['typegraph'] not in tps:
            raise Exception("Only bool type in 'typegraph'.")

        if not isinstance(fl_graph['weighted'], bool):
            raise Exception("Only bool type in 'weighted'.")

        if not isinstance(fl_graph['edge_id'], bool):
            raise Exception("Only bool type in 'edge_id'.")

        if not isinstance(fl_graph['nodes'], list):
            raise Exception("Only list type in 'nodes'.")

        if not isinstance(fl_graph['edges'], list):
            raise Exception("Only list type in 'edges'.")

        self._graph_id = fl_graph['graph_id']
        self._typegraph = fl_graph['typegraph']
        self._weighted = fl_graph['weighted']
        edge_id = fl_graph['edge_id']
        nodes = fl_graph['nodes']
        edges = fl_graph['edges']

        # reset values
        self._node = {}
        self._edge = {}

        # add nodes
        self.add_node(nodes)

        # add edges
        if self._weighted:
            if edge_id:
                for ed in edges:
                    self.add_edge(ed[0], ed[1], ed[2], ed[3])
            else:
                for ed in edges:
                    self.add_edge(None, ed[0], ed[1], ed[2])
        else:
            if edge_id:
                for ed in edges:
                    self.add_edge(ed[0], ed[1], ed[2])
            else:
                for ed in edges:
                    self.add_edge(None, ed[0], ed[1])
                 
    
    def save(self, filename):
        '''
        @brief save configuration in .json
        @param filename (str): name file
        >>> DEV...
        '''
        
        try:
            fl = open(filename, 'w')
            #fl_graph = json.load(fl)
            #fl.close()
        except:
            raise Exception('Error in file read/write.')
            
        #
        data = {}
        data['graph_id'] = self._graph_id
        data['typegraph'] = self._typegraph
        data['weighted'] = str(self.weighted).lower()
        data['edge_id'] = True
        data['nodes'] = [i for i in self._node]
        
        


