class SimpleNetwork:
    def __init__(self):
        self.queues = {}

    def register_node(self, node_id):
        self.queues[node_id] = []

    def send(self, sender_id, receiver_id, message):
        self.queues[receiver_id].append((sender_id, message))

    def receive(self, node_id):
        if self.queues[node_id]:
            return self.queues[node_id].pop(0)
        return None
