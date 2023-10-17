from .node import Node

class NodeManager:
    def __init__(self, network):
        self.nodes = {}
        self.network = network

    def create_node(self, node_id):
        node = Node(node_id, self.network)
        self.nodes[node_id] = node
        self.network.register_node(node_id)
        return node

    def list_nodes(self):
        return list(self.nodes.keys())
