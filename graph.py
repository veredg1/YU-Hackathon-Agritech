import networkx

class Node(object): #the graph is made up of nodes so we aren't going to want nodes outside of the graph anyway
            
        def Node(self, name,label,supply,demand):
                self._name = name  #name of the connection
                self._label = label #is it a producer or a supplier? 
                self._neighbors = [None] 
                self._supply = supply
                self._demand = demand 
                self._privateKey = 0
                self._publicKey = 0 #default values for now
        
        
        
        def getSupply(self):
            return self._supply
        
        
        def getDemand(self):
            return self._demand
        
        
        
        def changeSupply(self):
            self._supply = input()
        
        
        def changeDemand(self):
            self._demand = input()
        
                
            def addEdge(self,n):
                pass 
        
            def getNeighbors(self): 
                returnVal = []
                for v in self._neighbors:
                    if v._label != self._label:
                        returnVal += [v._label]
            
                return returnVal 
        
        
            def getLabel(self):
                return self._label 


        

    
def main():
     G = networkx.Graph(incoming_graph_data = None)
