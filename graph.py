# -----------------------------------------------------
# graph.py
# Author: Jhonathan Paulo Banczek.
# jhoonb.com - jpbanczek@gmail.com
# Python 3 >
# Data: 25/04/2014
# Last Update: 02/06/2014
# STATUS: Em desenvolvimento -
# -------- REFERENCIA ---------------------------------
# http://en.wikipedia.org/wiki/Graph_theory
# http://pt.wikipedia.org/wiki/Teoria_dos_grafos
#-------------------------------------------------------

from itertools import combinations


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

    def __init__(self, name='Graph', typegraph='graph', weighted=False):
        """
        id: identificador do grafo (str)
        typegraph: 'graph', 'tree', 'hipergraph'
        weighted: grafo ponderado (bool)
        """
        self._name = name
        self._typegraph = typegraph
        self._weighted = weighted
        self._node = {}
        self._edge = {}
        
    
    def exist_node(self, node, tp='any'):
        """
        verifica se exist node(vertice) no grafo
        tp-> type: all, any
        """
        
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
        """
        verifica se exist edge(aresta) no grafo
        edge pode ser uma lista ou uma str
        """
        
        if isinstance(edge, list):
            #edge = [str(i) for i in edge]
            
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
        """
        Adiciona um vértice ao grafo.
        Retorna: bool.
        """
        
        # apenas str
        if isinstance(node, (int, float)):
            node = str(node)
        elif isinstance(node, list):
            node = [str(i) for i in node]
        else:
            raise Exception(_error_[9])
            
        #se ja existe algum elemento de v no grafo
        if self.exist_node(node):
            raise Exception(_error_[0])
        
        if not self._weighted:
            weight = [0 for i in node]
            
        #se algum elemento de weight nao for numero retorna true
        check = all([isinstance(i, (int, float)) for i in weight])
        
        print(len(node), len(weight), check)
        
        if len(node) == len(weight) and check:
            for i in range(len(node)):
                self._node[node[i]] = [node[i], weight[i]]
        else:
            raise Exception(_error_[1])


    def add_edge(self, edge, node_origin, node_destiny, weight=0):
        """
        Adiciona uma aresta ao grafo.
        retorno: bool.
        """

        # elementos str
        node_origin, node_destiny = str(node_origin), str(node_destiny)

        # se for None cria o e
        if edge is None:
            edge = node_origin + node_destiny

        # se a aresta ja existe no grafo
        if self.exist_edge(edge):
            raise Exception(_error_[2])

        #se os vértices n existem no grafo
        if not self.exist_node([node_origin, node_destiny], 'all'):
            raise Exception(_error_[3])
            
        # verifica o tipo de w
        if isinstance(weight, (int, float)):
            self._edge[edge] = [node_origin, node_destiny, weight]
        else:
            raise Exception(_error_[4])


    def show(self):
        """ Exibe os vértices e arestas do grafo """

        print('*' * 60)

        print('Graph name:' , self._name)
        print(' -> Is Weighted: ', self._weighted)
        print(' -> Type Graph: ', self._typegraph)
        print('-' * 60)

        print('Nodes:','\n Id  |-|  Weight')
        for i in self._node:
            print(i, ': -> ', self._node[i])

        print('Edges:', '\n Id  |-| Origin | Destiny | Weight')
        for i in self._edge:
            print(i, ': -> ', self._edge[i])

        print('*' * 60)


    def order(self):
        """
        retorna (int) a cadinalidade do conjunto de vértices
        """
        return len(self._node)


    def size(self):
        """
        Retorna (int) a cardinalidade do conjunto de arestas.
        """
        return len(self._edge)


    def update_node_weight(self, node, weight):
        """
        Atualiza o peso do vértice.
        retorno: bool.
        """
        
        # str
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

        for i in self._edge:
            if self._edge[i][0] == node_x or self._edge[i][0] == node_y:
                if self._edge[i][1] == node_x or self._edge[i][1] == node_y:
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

        out = []
        
        for i in self._edge:
            if self._edge[i][0] == node:
                out.append(self._edge[i][1])
            elif self._edge[i][1] == node:
                out.append(self._edge[i][0])

        # se for vizinhança aberta
        if neighbourhood_open:
            return out
        else:
            out.insert(0, node)
            return out


    def complement(self):
        """
        Retorna (objeto: Graph) com o grafo complementar
        """

        # conjunto de vértices
        nodes = [i for i in self._node]

        #conjunto de arestas
        edges = [[self._edge[i][0], self._edge[i][1]] for i in self._edge]

        # todas as combinações possiveis de arestas
        total_edges = list(combinations(''.join(nodes), 2))
        #tupla -> lista
        total_edges = [list(i) for i in total_edges]

        #lambda function: verifica se a aresta está no conjunto
        # se x0,x1 e x1,x0 (inverso)
        _comp = lambda x: x in edges or [x[1], x[0]] in edges

        #conjunto de arestas que estão no grafo completo de G
        #e não estão em G
        complement = [i for i in total_edges if not _comp(i)]

        #cria um novo grafo
        gc = Graph(id='Complement of '+self._name)
        
        #add os vértices
        gc.add_node(nodes)
        
        for i in complement:
            gc.add_edge(None, i[0], i[1], None)

        return gc
    
    
    def complete(self):
        """
        retorna o grafo completo do grafo G
        """        
        g_complement = self.complement()
        
        g_complete = Graph(id="K")
        
        g_complete._node.update(self._node)
        g_complete._node.update(g_complement._node)
        
        g_complete._edge.update(self._edge)
        g_complete._edge.update(g_complement._edge)
        
        g_complement = None
        
        return g_complete
        

    def is_complete(self):
        """
        Retorna (bool) se o grafo é completo.
        em desenvolvimento...
        """

        if self._digraph:
            print(_error_[8])
            return False

        # conjunto de vértices
        vtx = [i for i in self._node]

        #conjunto de arestas
        edg = [[self._edge[i][0], self._edge[i][1]] for i in self._edge]

        # todas as combinações possiveis de arestas
        ttvtx = list(combinations(''.join(vtx), 2))
        #tupla -> lista
        ttvtx = [list(i) for i in ttvtx]

        edg.sort()
        ttvtx.sort()
        print(edg)
        print(ttvtx)

        print(edg == ttvtx)


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

        edge = []

        # adiciona as arestas que serão excluidas
        for i in self._edge:
            if self._edge[i][0] == node or self._edge[i][1] == node:
                edge.append(i)

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
        if not self.exist_node(edge):
            print(_error_[7])
            return False

        del self._edge[edge]

        return True


    def dijkstra(self, x, w):
        """
        Algoritmo de Dijkstra para o menor caminho em um grafo.
        O Grafo tem que ser ponderado (conter pesos) e não pode ter
        pesos negativos.
        """
        pass 
    
#---------------------------------------------------------------------


class Digraph(Graph, object):
    
    def __init__(self, name='Digraph', typegraph='graph', weighted=False):
        Graph.__init__(self, name, typegraph, weighted)
        
    
    def is_adjacent(self, node_x, node_y):
        
        #verifica se os n vértices existem no grafo
        if not self.exist_node([node_x, node_y], 'all'):
            raise Exception(_error_[3])
            
        for i in self._edge:
            if self._edge[i][0] == node_x and self._edge[i][1] == node_y:
                return True
            
        return False
    
    
    def complement(self):
        raise Exception(_error_[8])
    
    
    def complete(self):
        raise Exception(_error_[8])
        
        
    def neighbourhood(self, node, neighbourhood_open=True):
        """
        Retorna (list) a vizinhança do vértice node.
        neighbourhood_open: True -> vizinhança aberta, False: fechada.
        """
        
        #str
        node= str(node)
        
        #verifica se o vértice existe no grafo
        if not self.exist_node(node):
            raise Exception(_error_[3])

        out = []
        
        for i in self._edge:
            if self._edge[i][0] == node:
                out.append(self._edge[i][1])
                
        # se for vizinhança aberta
        if neighbourhood_open:
            return out
        else:
            out.insert(0, node)
            return out
        
#----------------------------------------------------------------------        
        