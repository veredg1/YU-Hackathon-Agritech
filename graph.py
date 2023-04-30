from .localstore import NodeBody

class Graph(object):
        class Node(object): #the graph is made up of nodes so we aren't going to want nodes outside of the graph anyway
            
                def Node(self, body: NodeBody):
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
                
                def changeLabel(self):
                        self._label = input("enter s if supplier, enter p if producer, enter c if consumer ")

                def changeSupply(self):
                        self._body.supply[input("name of what you have to offer?")] = input("quantity")


                def changeDemand(self):
                        self._body.supply[input("name of what you need?")] = input("quantity")
    
        def __init__(self):
                self._nodes = []
                
                
        def Traverse(self):
                pass
                
        def insert(self,n):
                pass 
        
        
        
    
    
    
    
    
        
    
        
    
        
    
        
        
        
        
        
        
    
    
