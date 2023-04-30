from dataclasses import dataclass
from enum import Enum

#three possibilities for what type of node each user is
class nodetype(Enum):
    PRODUCER = 0
    SUPPLIER = 1
    CONSUMER = 2

#magnitudes are how much of each type of produce each node needs/produces
@dataclass
class NodeBody:
    name: str = "defaultname"
    type: nodetype = nodetype.PRODUCER
    IP: str = "192.168.1.1"
    supply: dict = {}
    demand: dict = {}
    neighbors: list = []

#TODO: incorporate private key signing into this data class