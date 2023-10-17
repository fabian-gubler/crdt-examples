def generate_node_id():
    """Generate a unique node ID. For simplicity, we'll use incremental integers."""
    # This is a simple counter-based approach. In a real system, this might be UUIDs or something more robust.
    global node_counter
    node_counter += 1
    return node_counter

node_counter = 0
