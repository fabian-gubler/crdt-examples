from .message import Message
from crdts.gcounter import GCounter
from crdts.pncounter import PNCounter
from crdts.lwwregister import LWWRegister

class Node:
    def __init__(self, node_id, network):
        self.node_id = node_id
        self.network = network
        self.gcounter = GCounter(node_id)
        self.pncounter = PNCounter(node_id)
        self.lwwregister = LWWRegister(node_id)

    def send_state(self, crdt_type):
        if crdt_type == "gcounter":
            message = Message(self.node_id, "gcounter_state", self.gcounter)
        elif crdt_type == "pncounter":
            message = Message(self.node_id, "pncounter_state", self.pncounter)
        elif crdt_type == "lwwregister":
            message = Message(self.node_id, "lwwregister_op", {"value": self.lwwregister.get(), "version_vector": self.lwwregister.version_vector})
        self.network.send(message)

    def receive_state(self):
        message = self.network.receive()
        if message:
            if message.operation == "gcounter_state":
                self.gcounter.merge(message.data)
            elif message.operation == "pncounter_state":
                self.pncounter.merge(message.data)
            elif message.operation == "lwwregister_op":
                self.lwwregister.apply_operation(message)
