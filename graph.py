import rsa
import networkx

class Node(object): 
    
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
        
        
    def addNeighbor(self,n):
        pass
    
    def getNeighbors(self): 
        
        pass 
    
    def getLabel(self):
        return self._label 
    
    
    
    
    
    
        
    
        
    
        
    
        
        
        
        
        
        
    
    
