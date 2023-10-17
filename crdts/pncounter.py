from .gcounter import GCounter

class PNCounter:
    def __init__(self, node_id):
        self.p_counter = GCounter(node_id)
        self.n_counter = GCounter(node_id)

    def increment(self):
        """Increment the positive counter."""
        self.p_counter.increment()

    def decrement(self):
        """Increment the negative counter."""
        self.n_counter.increment()

    def value(self):
        """Get the current value of the counter."""
        return self.p_counter.value() - self.n_counter.value()

    def merge(self, other):
        """Merge another PNCounter into this one."""
        self.p_counter.merge(other.p_counter)
        self.n_counter.merge(other.n_counter)
