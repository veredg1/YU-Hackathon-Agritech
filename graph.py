from localstore import NodeBody
import networx

class Graph(object):
        class Node(object): #the graph is made up of nodes so we aren't going to want nodes outside of the graph anyway
            
                def _init__(self, body: NodeBody):
                        self._body = body

                def getSupply(self):
                        return self._body.supply
        
                def getDemand(self):
                        return self._body.demand
        
                def addEdge(self,n):
                        pass 
        
                def getNeighbors(self): 
                        returnVal = []
                        for v in self._body.neighbors:
                                if v._label != self._label:
                                        returnVal += [v._label]
            
                        return returnVal 
        
        
                def getLabel(self):
                        return self._label 
    
        def __init__(self):
                self._nodes = []
                
                
        def traverse(self):
                networkx.bfs_edges(self)
                
        def insert(self,n):
                self.nodes.append(n)
                
        
        
        
    
    
    
    
    
        
    
        
    
        
    
        
        
        
        
        
        
    
    
