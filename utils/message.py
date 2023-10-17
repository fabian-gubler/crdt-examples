class Message:
    def __init__(self, sender_id, operation, data):
        self.sender_id = sender_id
        self.operation = operation  # e.g. 'increment', 'set'
        self.data = data  # e.g. counter value, register value
