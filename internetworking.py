from .localstore import NodeBody
import rsa

#gets the nodebody from a given IP. 
def requestInfo(IP:str) -> NodeBody:
    #return stuff about IP, implement later
    return NodeBody()

#encrypts the bytes with the given IP's private key. 
def handshake(IP:str, b:bytes) -> bytes:
    return rsa.encrypt(bytes,requestInfo(IP).public_key)

def getNeighbors(IP:str):
    return requestInfo(IP).neighbors
