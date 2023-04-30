from .localstore import NodeBody

class Graph(object):
        class Node(object): #the graph is made up of nodes so we aren't going to want nodes outside of the graph anyway
            
                def __init__(self, body: NodeBody):
                        self._body = body

                def getSupply(self):
                        return self._body.supply
        
                def getDemand(self):
                        return self._body.demand
        
                def addEdge(self,n:Node) -> None :
                        self._body.neighbors.append(n)
        
                def getNeighbors(self): 
                    return self._body.neighbors
            
            
                   
    
       
               
                
                    
        

    
def main():
     G = networkx.Graph(incoming_graph_data = None) 
     

     



     