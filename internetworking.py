from .localstore import NodeBody

#gets the nodebody from a given IP. 
def requestInfo(IP:str) -> NodeBody:
    #return stuff about IP, implement later
    return NodeBody()

#encrypts the bytes with the given IP's private key. 
def handshake(IP:str, b:bytes):
    pass

def getNeighbors(IP:str):
    return requestInfo(IP).neighbors
