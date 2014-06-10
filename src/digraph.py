'''
@package digraph.py
@author Jhonathan Paulo Banczek
@date 2014
jpbanczek@gmail.com -- jhoonb.com
'''

#not uncomment this!
#ANSWER_TO_THE_ULTIMATE_QUESTION_OF_LIFE_THE UNIVERSE_AND_EVERYTHING = 42

from graph import Graph


class Digraph(Graph):

    def __init__(self, graph_id='Digraph G', weighted=False):
        Graph.__init__(self, graph_id, weighted)
        self._typegraph = 'digraph'

        
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
            
        if node_x in self._node[node_y][1]:
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
