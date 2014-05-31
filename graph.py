# -----------------------------------------------------
# graph.py
# Author: Jhonathan Paulo Banczek.
# jhoonb.com - jpbanczek@gmail.com
# Python 3 >
# Data: 25/04/2014
# Last Update: 01/05/2014
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
           8: 'Error [8]: Apenas Grafos Simples.'
}

class Graph(object):

    def __init__(self, id='Graph', typegraph='graph', digraph=False, weighted=False):
        """
        id: identificador do grafo (str)
        typegraph: 'graph', 'tree', 'hipergraph'
        digraph: grafo direcionado -> digrafo (bool)
        weighted: grafo ponderado (bool)
        """
        self._id = id
        self._typegraph = typegraph
        self._digraph = digraph
        self._weighted = weighted
        self._vtx = {}
        self._edg = {}
        
    
    def exist_node(self, v, t='any'):
        """
        verifica se exist v(vertice) no grafo
        v pode ser uma lista ou uma str
        """
        
        if isinstance(v, list):
            v = [str(i) for i in v]
            if t is 'any':
                if any([i in self._vtx for i in v]):
                    return True
            else:
                if all([i in self._vtx for i in v]):
                    return True
        else:
            v = str(v)
            if v in self._vtx:
                return True
        
        return False
    
    
    def exist_edge(self, e, t='any'):
        """
        verifica se exist e(aresta) no grafo
        e pode ser uma lista ou uma str
        """
        
        if isinstance(e, list):
            e = [str(i) for i in e]
            
            if t is 'any':
                if any([i in self._edg for i in e]):
                    return True
            else:
                if all([i in self._edg for i in e]):
                    return True
        else:
            e = str(e)
            if e in self._edg:
                return True
        
        return False
    
    

    def add_node(self, v, w=None):
        """
        Adiciona um vértice ao grafo.
        Retorna: bool.
        """

        #se ja existe algum elemento de v no grafo
        if self.exist_node(v):
            print(_error_[0])
            return False
        
        #str elementos
        v = [str(i) for i in v]

        #verifica graph ponderado
        if self._weighted:

            #se algum elemento de w nao for numero retorna true
            check = not any([isinstance(i, (int, float)) for i in w])

            if len(v) == len(w) and check:
                for i in range(len(v)):
                    self._vtx[v[i]] = [v[i], w[i]]
            else:
                print(_error_[1])
                return False
        #graph simple
        else:
            for i in range(len(v)):
                self._vtx[v[i]] = [v[i], None]

        return True


    def add_edge(self, id, o, d, w=None):
        """
        Adiciona uma aresta ao grafo.
        retorno: bool.
        """

        # elementos str
        o, d = str(o), str(d)

        # se for None cria o id
        if id is None:
            id = o+d

        # se a aresta ja existe no grafo
        if self.exist_edge(id):
            print(_error_[2])
            return False

        #se os vértices n existem no grafo
        if not self.exist_node([o, d], 'all'):
            print(_error_[3])
            return False

        # se for grafo ponderado
        if self._weighted:

            # verifica o tipo de w
            if isinstance(w, (int, float)):
                self._edg[id] = [o, d, w]
            else:
                print(_error_[4])
                return False
        else:
            self._edg[id] = [o, d, None]
            
        return True


    def show(self):
        """ Exibe os vértices e arestas do grafo """

        print('*' * 60)

        print('Graph id:' , self._id)
        print(' -> Is Digraph: ', self._digraph)
        print(' -> Is Weighted: ', self._weighted)
        print(' -> Type Graph: ', self._typegraph)
        print('-' * 60)

        print('Nodes:','\n Id  |-|  Weight')
        for i in self._vtx:
            print(i, ': -> ', self._vtx[i])

        print('Edges:', '\n Id  |-| Origin | Destiny | Weight')
        for i in self._edg:
            print(i, ': -> ', self._edg[i])

        print('*' * 60)


    def order(self):
        """
        retorna (int) a cadinalidade do conjunto de vértices
        """
        return len(self._vtx)


    def size(self):
        """
        Retorna (int) a cardinalidade do conjunto de arestas.
        """
        return len(self._edg)


    def update_node_w(self, id, w):
        """
        Atualiza o peso do vértice.
        retorno: bool.
        """

        if not self._weighted:
            print(_error_[5])
            return False
        
        if not self.exist_node(id):
            print(_error_[3])
            return False

        if not isinstance(w, (int, float)):
            print(_error_[4])
            return False

        self._vtx[id][1] = w

        return True


    def update_edge_w(self, id, w):
        """
        Atualiza o peso da aresta.
        retorno: bool.
        """

        #verifica se é um grafo ponderado
        if not self._weighted:
            print(_error_[5])
            return False

        #verifica se existe a aresta no grafo
        if not self.exist_node(id):
            print(_error_[7])
            return False

        #verifica se o tipo de w é válido
        if not isinstance(w, (int, float)):
            print(_error_[4])
            return False

        self._edg[id][2] = w

        return True


    def is_adjacent(self, x, w):
        """
        Retorna (bool) se o vértice x é adjacente
        ao vértice w.
        """

        #verifica se os n vértices existem no grafo
        if not self.exist_node([x, w], 'all'):
            print(_error_[3])
            return False  

        #grafo simples
        if not self._digraph:
            for i in self._edg:
                if self._edg[i][0] == x or self._edg[i][0] == w:
                    if self._edg[i][1] == x or self._edg[i][1] == w:
                        return True
        #digrafo
        else:
            for i in self._edg:
                if self._edg[i][0] == x and self._edg[i][1] == w:
                    return True

        return False


    def neighbourhood(self, x, neighbourhood_open=True):
        """
        Retorna (list) a vizinhança do vértice x.
        neighbourhood_open: True -> vizinhança aberta, False: fechada.
        """

        #verifica se o vértice existe no grafo
        if not self._node(x):
            print(_error_[3])
            return False

        out = []

        # se for um digrafo
        if self._digraph:
            for i in self._edg:
                if self._edg[i][0] == x:
                    out.append(self._edg[i][1])

        # se for grafo simples
        else:
            for i in self._edg:
                if self._edg[i][0] == x:
                    out.append(self._edg[i][1])
                elif self._edg[i][1] == x:
                    out.append(self._edg[i][0])

        # se for vizinhança aberta
        if neighbourhood_open:
            return out
        else:
            out.insert(0, x)
            return out


    def complement(self):
        """
        Retorna (objeto: Graph) com o grafo complementar
        """

        if self._digraph:
            print(_error_[8])
            return False

        # conjunto de vértices
        vtx = [i for i in self._vtx]

        #conjunto de arestas
        edg = [[self._edg[i][0], self._edg[i][1]] for i in self._edg]

        # n. de arestas que faltam pra completar o grafo
        #tt = ((self.order() * (self.order() - 1))/2 ) - len(vtx)

        # todas as combinações possiveis de arestas
        ttvtx = list(combinations(''.join(vtx), 2))
        #tupla -> lista
        ttvtx = [list(i) for i in ttvtx]

        #lambda function: verifica se a aresta está no conjunto
        # se x0,x1 e x1,x0 (inverso)
        _comp = lambda x: x in edg or [x[1], x[0]] in edg

        #conjunto de arestas que estão no grafo completo de G
        #e não estão em G
        complement = [i for i in ttvtx if not _comp(i)]

        #cria um novo grafo
        gc = Graph(id='Complement of '+self._id)
        #add os vértices
        gc.add_node(vtx)
        for i in complement:
            gc.add_edge(None, i[0], i[1], None)

        return gc
    
    def complete(self):
        """
        retorna o grafo completo do grafo G
        """
        
        #verifica se é um grafo simples
        if not self._typegraph is 'graph':
            print(_error_[8])
            return False
        
        g_complement = self.complement()
        
        g_complete = Graph(id="K")
        
        g_complete._vtx.update(self._vtx)
        g_complete._vtx.update(g_complement._vtx)
        
        g_complete._edg.update(self._edg)
        g_complete._edg.update(g_complement._edg)
        
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
        vtx = [i for i in self._vtx]

        #conjunto de arestas
        edg = [[self._edg[i][0], self._edg[i][1]] for i in self._edg]

        # todas as combinações possiveis de arestas
        ttvtx = list(combinations(''.join(vtx), 2))
        #tupla -> lista
        ttvtx = [list(i) for i in ttvtx]

        edg.sort()
        ttvtx.sort()
        print(edg)
        print(ttvtx)

        print(edg == ttvtx)


    def del_node(self, x):
        """
        deleta o vértice x do grafo.
        consequentemente deleta as arestas que contem x.
        retorno: Bool
        """

        #verifica se o vértice existe no grafo
        if not self._node(x):
            print(_error_[3])
            return False

        edg = []

        # adiciona as arestas que serão excluidas
        for i in self._edg:
            if self._edg[i][0] == x or self._edg[i][1] == x:
                edg.append(i)

        #ignore spam
        # apaga as arestas que tinham relação com x
        spam = [self._edg.pop(i) for i in edg]
        spam, edg = None, None

        #deleta o vértice
        del self._vtx[x]

        return True


    def del_edge(self, xy):
        """
        deleta a aresta xy do grafo.
        Retorno: Bool
        """

        #verifica se existe a aresta no grafo
        if not self.exist_node(xy):
            print(_error_[7])
            return False

        del self._edg[xy]

        return True


    def dijkstra(self, x, w):
        """
        Algoritmo de Dijkstra para o menor caminho em um grafo.
        O Grafo tem que ser ponderado (conter pesos) e não pode ter
        pesos negativos.
        """
        pass
#---------------------------------------------------------------------
