class VersionVector:
    def __init__(self):
        # A dictionary with node_id as key and its logical clock as value.
        self.vector = {}

    def increment(self, node_id):
        """Increment the logical clock for a given node_id."""
        self.vector[node_id] = self.vector.get(node_id, 0) + 1

    def update(self, other_vector):
        """Merge another version vector into this one."""
        for node, clock in other_vector.vector.items():
            self.vector[node] = max(self.vector.get(node, 0), clock)

    def is_greater_than(self, other_vector):
        """Check if this vector is strictly greater than another vector."""
        for node, clock in other_vector.vector.items():
            if self.vector.get(node, 0) <= clock:
                return False
        return True
