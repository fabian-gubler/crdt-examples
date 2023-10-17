class SimpleNetwork:
    def __init__(self):
        self.queue = []

    def send(self, message):
        """Simulate sending a message by adding it to a queue."""
        self.queue.append(message)

    def receive(self):
        """Simulate receiving a message by popping it from the queue."""
        return self.queue.pop(0) if self.queue else None
