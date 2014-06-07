from graph import Graph


class Digraph(Graph, object):

    def __init__(self, name='Digraph', weighted=False):
        Graph.__init__(self, name, weighted)
        self.typegraph = 'digraph'


    def is_adjacent(self, node_x, node_y):

        #verifica se os n vértices existem no grafo
        if not self.exist_node([node_x, node_y], 'all'):
            raise Exception(_error_[3])
        
        if node_y in self._node[node_x][1]:
            return True
        
        return False

    
    def complement(self):
        raise Exception(_error_[8])

        
    def complete(self):
        raise Exception(_error_[8])
        
        
    def is_complete(self):
        raise Exception(_error_[8])
