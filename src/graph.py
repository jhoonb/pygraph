'''
@package graph.py
@author Jhonathan Paulo Banczek
@date 2014
jpbanczek@gmail.com -- jhoonb.com
'''

from itertools import combinations

'''
@brief define errors
'''
_error_ = { 0: 'Error [0]: Já existe o vértice no Grafo',
           1: 'Error [1]: N. de vértices e n. de pesos não iguais',
           2: 'Error [2]: já existe essa aresta no grafo.',
           3: 'Error [3]: Não existe esse vértice no grafo',
           4: 'Error [4]: w não é um valor válido',
           5: 'Error [5]: Não é um grafo ponderado.',
           7: 'Error [7]: Não existe essa aresta no grafo.',
           8: 'Error [8]: Apenas Grafos Simples.',
           9: 'Error [9]: Valor do vértice apenas do tipo str'
}

class Graph(object):
    '''
    @brief class Graph
    '''

    def __init__(self, graph_id='Graph', weighted=False):
        '''
        @param graph_id (str): id of graph
        @param weighted (bool): if graph is weighted
        '''
        
        self._graph_id = graph_id
        self.typegraph = 'graph'
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

        # create id edge
        if edge is None:
            edge = node_origin + node_destiny

        # check if edge exist in graph
        if self.exist_edge(edge):
            raise Exception(_error_[2])

        # check if nodes not exist in graph
        if not self.exist_node([node_origin, node_destiny], 'all'):
            raise Exception(_error_[3])

        # check weight type, only int or float
        if isinstance(weight, (int, float)):
            
            self._edge[edge] = [node_origin, node_destiny, weight]
            # insert adjacency list
            self._node[node_origin][1].append(node_destiny)
        else:
            raise Exception(_error_[4])

            
    def show(self):
        """ Exibe os vértices e arestas do grafo """

        print('*' * 60)

        print('Graph graph_id:' , self._graph_id)
        print(' -> Is Weighted: ', self.weighted)
        print(' -> Type Graph: ', self.typegraph)
        print('-' * 60)

        print('Nodes:','\n Id  |-|  Weight')
        for i in self._node:
            print(i, ': -> ', self._node[i])

        print('Edges:', '\n Id  |-| Origin | Destiny | Weight')
        for i in self._edge:
            print(i, ': -> ', self._edge[i])

        print('*' * 60)


    def order(self):
        '''
        @brief cardinality of the set of nodes
        @return int
        '''
        return len(self._node)


    def size(self):
        '''
        @brief cardinality of the set of edges
        @return int
        '''
        return len(self._edge)


    def update_node_weight(self, node, weight):
        """
        Atualiza o peso do vértice.
        retorno: bool.
        """

        # only str
        node = str(node)

        if not self.exist_node(node):
            raise Exception(_error_[3])

        if not isinstance(w, (int, float)):
            raise Exception(_error_[4])

        self._node[node][1] = weight


    def update_edge_weight(self, edge, weight):
        """
        Atualiza o peso da aresta.
        retorno: bool.
        """

        #str
        edge = str(edge)

        #verifica se existe a aresta no grafo
        if not self.exist_node(edge):
            raise Exception(_error_[7])

        #verifica se o tipo de weight é válido
        if not isinstance(weight, (int, float)):
            raise Exception(_error_[4])

        self._edge[edge][2] = weight


    def is_adjacent(self, node_x, node_y):
        """
        Retorna (bool) se o vértice node_x é adjacente
        ao vértice node_y.
        """

        #str
        node_x, node_y = str(node_x), str(node_y)

        #verifica se os n vértices existem no grafo
        if not self.exist_node([node_x, node_y], 'all'):
            raise Exception(_error_[3])

        if node_y in self._node[node_x][1] or node_x in self._node[node_y][1]:
            return True
        
        return False


    def neighbourhood(self, node, neighbourhood_open=True):
        """
        Retorna (list) a vizinhança do vértice node.
        neighbourhood_open: True -> vizinhança aberta, False: fechada.
        """

        #str
        node = str(node)

        #verifica se o vértice existe no grafo
        if not self.exist_node(node):
            raise Exception(_error_[3])
            
        output = [i for i in self._node if self.is_adjacent(i, node)]
        
        #output = self._node[node][1]
        
        if neighbourhood_open:
            return output
        else:
            output.insert(0, node)
            return output
        

    def complement(self):
        """
        Retorna (objeto: Graph) com o grafo complementar
        """

        #conjunto de arestas
        edges = [(self._edge[i][0], self._edge[i][1]) for i in self._edge]

        # todas as combinações possiveis de arestas
        # arestas do grafo Completo.
        total_edges = list(combinations([i for i in self._node], 2))
        total_edges = [i for i in total_edges if not i[0] == i[1]]

        #lambda function-> busca(x), se alguma aresta x(e sua inversa) for encontrada
        # no conjunto edges de arestas retorna True
        busca = lambda x: any([True for i in edges if i == x or (i[1],i[0]) == x])

        #compl -> conjunto de arestas do grafo complementar,
        # arestas que nao estão no grafo G dado e estão no grafo Completo
        compl = [i for i in total_edges if busca(i) is False]

        #cria um novo grafo
        gc = Graph(graph_id='Complement of '+self._graph_id)

        #add os vértices
        gc.add_node([i for i in self._node])

        for i in compl:
            gc.add_edge(None, i[0], i[1], 0)

        return gc


    def complete(self):
        """
        retorna o grafo completo do grafo G
        """

        #conjunto de arestas
        edges = [(self._edge[i][0], self._edge[i][1]) for i in self._edge]

        # todas as combinações possiveis de arestas
        # arestas do grafo Completo.
        total_edges = list(combinations([i for i in self._node], 2))
        # menos as arestas com loop
        total_edges = [i for i in total_edges if not i[0] == i[1]]

        g_complete = Graph(graph_id="Complete")

        g_complete.add_node([i for i in self._node])

        for i in total_edges:
            g_complete.add_edge(None, i[0], i[1], 0)

        return g_complete


    def is_complete(self):
        """
        Retorna (bool) se o grafo é completo.
        em desenvolvimento...
        """
        
        edges = [(self._edge[i][0], self._edge[i][1]) for i in self._edge]
        # todas as combinações possiveis de arestas
        # arestas do grafo Completo.
        total_edges = list(combinations([i for i in self._node], 2))
        # menos as arestas com loop
        total_edges = [i for i in total_edges if not i[0] == i[1]]
        final = [i for i in total_edges if not i in edges and not (i[1],i[0]) in edges]
        
        if len(final) == 0:
            return True
        else:
            return False


    def del_node(self, node):
        """
        deleta o vértice node do grafo.
        consequentemente deleta as arestas que contem node.
        retorno: Bool
        """

        #str
        node = str(node)

        #verifica se o vértice existe no grafo
        if not self.exist_node(node):
            raise Exception(_error_[3])

        edge = [i for i in self._edge if node in self._edge[i][:2]]

        # adiciona as arestas que serão excluidas
        #for i in self._edge:
        #    if self._edge[i][0] == node or self._edge[i][1] == node:
        #        edge.append(i)

        # apaga as arestas que tinham relação com node
        edge = [self._edge.pop(i) for i in edge]
        edge = None

        #deleta o vértice
        del self._node[node]

        return True


    def del_edge(self, edge):
        """
        deleta a aresta edge do grafo.
        Retorno: Bool
        """

        #str
        edge = str(edge)

        #verifica se existe a aresta no grafo
        if not self.exist_edge(edge):
            raise Exception(_error_[7])

        del self._edge[edge]

        return True


    def dijkstra(self, x, w):
        """
        Algoritmo de Dijkstra para o menor caminho em um grafo.
        O Grafo tem que ser ponderado (conter pesos) e não pode ter
        pesos negativos.
        """
        pass
    
    
    def dfs(self):
        pass

        
    def bfs(self):
        pass
    
    def line_graph(self):
        pass

#---------------------------------------------------------------------
