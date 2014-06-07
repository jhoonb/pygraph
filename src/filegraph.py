import configparser

class FileGraph(object):
    
    def __init__(self):
        
        self._conf = configparser.ConfigParser()
        self._filename = ''
        self._conf['graph']['name'] = ''
        self._conf['graph']['typegraph'] = ''
        self._conf['graph']['weighted'] = ''
        self._conf['graph']['edges_name'] = ''
        self._conf['graph']['nodes'] = ''
        self._conf['graph']['edges'] = ''
    
    def load(self, filename):
        
        self._conf.read(filename)
        
    
    def save(self, filename):
        pass
        
        
    
    