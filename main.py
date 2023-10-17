from utils.node_id import generate_node_id
from utils.network import SimpleNetwork
from utils.node import Node
from utils.node_manager import NodeManager
from crdts.gcounter import GCounter
from crdts.pncounter import PNCounter
from crdts.lwwregister import LWWRegister


def main():
    network = SimpleNetwork()
    manager = NodeManager(network)

    while True:
        print("\nOptions: create_node, list_nodes, select_node, exit")
        choice = input("Choose an action: ")

        if choice == "create_node":
            node_id = generate_node_id()
            manager.create_node(node_id)
            print(f"Node {node_id} created.")
        elif choice == "select_node":
            node_id_input = input("Enter node ID to select: ")
            try:
                node_id = int(node_id_input)
                if node_id in manager.nodes:
                    node_interaction(manager.nodes[node_id])
                else:
                    print("Invalid node ID.")
            except ValueError:
                print("Please enter a valid integer for node ID.")
        elif choice == "list_nodes":
            nodes = manager.list_nodes()
            if nodes:
                # Convert node IDs to strings before joining
                print("Created nodes:", ", ".join(map(str, nodes)))
            else:
                print("No nodes created yet.")
        elif choice == "exit":
            break

def node_interaction(node):
    while True:
        print(f"\nOptions for node {node.node_id}:")
        print("increment_gc, increment_pn, decrement_pn, set_lww, get_gc, get_pn, get_lww, send_state, receive_state, back")
        choice = input("Choose an action: ")

        if choice == "increment_gc":
            node.gcounter.increment()
            print("GCounter incremented.")

        elif choice == "increment_pn":
            node.pncounter.increment()
            print("PNCounter incremented.")

        elif choice == "decrement_pn":
            node.pncounter.decrement()
            print("PNCounter decremented.")

        elif choice == "set_lww":
            value = int(input("Enter a number to set in LWWRegister: "))
            node.lwwregister.set(value)
            print(f"LWWRegister set to {value}.")

        elif choice == "get_gc":
            print(f"GCounter value: {node.gcounter.get()}")

        elif choice == "get_pn":
            print(f"PNCounter value: {node.pncounter.get()}")

        elif choice == "get_lww":
            print(f"LWWRegister value: {node.lwwregister.get()}")

        elif choice == "send_state":
            crdt_type = input("Which CRDT state to send? (gcounter, pncounter, lwwregister): ")
            receiver_id = input("Enter receiver node ID: ")
            node.send_state(crdt_type, receiver_id)
            print(f"{crdt_type} state sent to node {receiver_id}.")

        elif choice == "receive_state":
            message = node.network.receive(node.node_id)
            if message:
                sender, (operation, data) = message
                if operation == "gcounter_state":
                    node.gcounter.merge(data)
                elif operation == "pncounter_state":
                    node.pncounter.merge(data)
                elif operation == "lwwregister_op":
                    node.lwwregister.apply_operation(data)
                print(f"State received and merged from node {sender}.")
            else:
                print("No messages for this node.")

        elif choice == "back":
            break

        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main()
