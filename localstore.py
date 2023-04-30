from enum import Enum
from .internetworking import handshake

#three possibilities for what type of node each user is
class nodetype(Enum):
    PRODUCER = 0
    SUPPLIER = 1
    CONSUMER = 2

#supply and demand are dicts from product names to ammounts (as yearly production/need)
class NodeBody:
    name: str = "defaultname"
    type: nodetype = nodetype.PRODUCER
    IP: str = "192.168.1.1"
    supply: dict = {}
    demand: dict = {}
    neighbors: list = []
    crypto: bytes = bytes(name, "utf-8")

    def addNeighbor(self, IP: str):
        self.crypto = handshake(IP, self.crypto)
        self.neighbors.append(IP)



#TODO: incorporate private key signing into this data class