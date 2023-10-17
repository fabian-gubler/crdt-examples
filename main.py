from utils.node_id import generate_node_id
from utils.network import SimpleNetwork
from utils.node import Node
from crdts.gcounter import GCounter
from crdts.pncounter import PNCounter
from crdts.lwwregister import LWWRegister


def main():
    network = SimpleNetwork()
    node_id = generate_node_id()
    node = Node(node_id, network)

    gcounter = GCounter(node_id)
    pncounter = PNCounter(node_id)
    lwwregister = LWWRegister(node_id)

    while True:
        print(
            "\nOptions: increment_gc, increment_pn, decrement_pn, set_lww, get_gc, get_pn, get_lww, send_state, receive_state, exit"
        )

        choice = input("Choose an action: ")

        if choice == "increment_gc":
            gcounter.increment()
            print("GCounter incremented.")
        elif choice == "increment_pn":
            pncounter.increment()
            print("PNCounter incremented.")
        elif choice == "decrement_pn":
            pncounter.decrement()
            print("PNCounter decremented.")
        elif choice == "set_lww":
            value = int(input("Enter a number to set in LWWRegister: "))
            lwwregister.set(value)
            print(f"LWWRegister set to {value}.")
        elif choice == "get_gc":
            print(f"GCounter value: {gcounter.value()}")
        elif choice == "get_pn":
            print(f"PNCounter value: {pncounter.value()}")
        elif choice == "get_lww":
            print(f"LWWRegister value: {lwwregister.get()}")
        elif choice == "send_state":
            crdt_type = input("Which CRDT state to send? (gcounter, pncounter, lwwregister): ")
            node.send_state(crdt_type)
            print(f"{crdt_type} state sent.")
        elif choice == "receive_state":
            node.receive_state()
            print("State received and merged.")
        elif choice == "exit":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
