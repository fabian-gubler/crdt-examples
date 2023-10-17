from utils.node_manager import NodeManager
from utils.network import SimpleNetwork
from crdts.version_vector import VersionVector

def automated_test():
    network = SimpleNetwork()
    manager = NodeManager(network)

    # Create two nodes
    node_1 = manager.create_node("Node_1")
    node_2 = manager.create_node("Node_2")

    # Perform operations on Node_1
    node_1.gcounter.increment()
    node_1.lwwregister.set(100)

    # Perform operations on Node_2
    node_2.pncounter.increment()
    node_2.pncounter.increment()
    node_2.lwwregister.set(150)

    # Send state from Node_1 to Node_2
    node_1.send_state("gcounter", "Node_2")
    node_1.send_state("lwwregister", "Node_2")

    # Merge states in Node_2
    message = node_2.network.receive(node_2.node_id)
    if message:
        sender, (operation, data) = message
        if operation == "gcounter_state":
            node_2.gcounter.merge(data)

    message = node_2.network.receive(node_2.node_id)
    if message:
        sender, (operation, data) = message
        if operation == "lwwregister_op":
            incoming_value = data["value"]
            incoming_version_vector = VersionVector()
            node_2.lwwregister.apply_operation(incoming_value, incoming_version_vector)

    # Display results
    print(f"Node_1 GCounter: {node_1.gcounter.get_state()}")
    print(f"Node_1 LWWRegister: {node_1.lwwregister.get()}")
    print(f"Node_2 GCounter: {node_2.gcounter.get_state()}")
    print(f"Node_2 PNCounter: {node_2.pncounter.get_state()}")
    print(f"Node_2 LWWRegister: {node_2.lwwregister.get_state()}")

if __name__ == "__main__":
    automated_test()
