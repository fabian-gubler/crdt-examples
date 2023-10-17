from .version_vector import VersionVector

class LWWRegister:
    def __init__(self, node_id):
        self.node_id = node_id
        self.value = None
        self.version_vector = VersionVector()

    def set(self, value):
        """Set a new value for the register."""
        self.value = value
        self.version_vector.increment(self.node_id)

    def get(self):
        """Get the current value of the register."""
        return self.value

    def get_state(self):
        """Get the current value of the register."""
        return self.value

    def apply_operation(self, incoming_value, incoming_version_vector):
        """Apply a received 'set' operation to the register."""
        if incoming_version_vector.is_greater_than(self.version_vector):
            self.value = incoming_value
            self.version_vector.update(incoming_version_vector)
