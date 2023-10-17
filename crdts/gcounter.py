from .version_vector import VersionVector

class GCounter:
    def __init__(self, node_id):
        self.node_id = node_id
        # A dictionary with node_id as key and its count as value.
        self.counts = {}
        self.version_vector = VersionVector()

    def increment(self):
        """Increment the counter for this node."""
        self.counts[self.node_id] = self.counts.get(self.node_id, 0) + 1
        self.version_vector.increment(self.node_id)

    def value(self):
        """Get the current value of the counter."""
        return sum(self.counts.values())

    def merge(self, other):
        """Merge another GCounter or its state into this one."""
        other_counts = other
        if isinstance(other, GCounter):
            other_counts = other.counts

        for node, count in other_counts.items():
            self.counts[node] = max(self.counts.get(node, 0), count)
        # If `other` is a GCounter object, update the version vector.
        if isinstance(other, GCounter):
            self.version_vector.update(other.version_vector)

    def get_state(self):
        return self.counts

    def get(self):
        return self.counts
