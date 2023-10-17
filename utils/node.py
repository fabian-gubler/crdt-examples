from .message import Message
from crdts.gcounter import GCounter
from crdts.pncounter import PNCounter
from crdts.lwwregister import LWWRegister

class Node:
    def __init__(self, node_id, network):
        self.node_id = node_id
        self.network = network

        # Initializing CRDTs
        self.gcounter = GCounter(node_id)
        self.pncounter = PNCounter(node_id)
        self.lwwregister = LWWRegister(node_id)

    def send_state(self, crdt_type, receiver_id):
        message = None

        if crdt_type == "gcounter":
            message = ("gcounter_state", self.gcounter.get_state())
        elif crdt_type == "pncounter":
            message = ("pncounter_state", self.pncounter.get_state())
        elif crdt_type == "lwwregister":
            message_content = {
                "value": self.lwwregister.get(),
                "version_vector": self.lwwregister.version_vector.get_state()
            }
            message = ("lwwregister_op", message_content)

        if message:
            self.network.send(self.node_id, receiver_id, message)
        else:
            print(f"Invalid CRDT type: {crdt_type}")

    def receive_state(self):
        data = self.network.receive(self.node_id)
        if not data:
            print("No message available.")
            return

        sender_id, message = data
        operation, content = message

        if operation == "gcounter_state":
            self.gcounter.merge(content)
        elif operation == "pncounter_state":
            self.pncounter.merge(content)
        elif operation == "lwwregister_op":
            # Assuming the LWWRegister's apply_operation method takes in the value and version vector
            self.lwwregister.apply_operation(content["value"], content["version_vector"])
        else:
            print(f"Invalid operation received: {operation}")
