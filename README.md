# CRDT Project

This repository contains a simple implementation of Convergent Replicated Data Types (CRDTs) to explore and understand their principles, operations, and use-cases in distributed systems.

## Implemented CRDTs

1. **GCounter**: A grow-only counter that allows increments. Implemented using a **state-based** approach.
2. **PNCounter**: A counter that supports both increments and decrements. Implemented using a **state-based** approach.
3. **LWWRegister**: A Last-Writer-Wins Register that resolves conflicts using timestamps and version vectors. Implemented using an **operational** approach.

## Features

- **Network Simulation**: A simple in-memory message queue simulating node-to-node communication.
- **Node Interaction**: Nodes can send and receive operations or states, depending on the CRDT type.
- **Conflict Resolution**: Demonstrated in the LWWRegister using timestamps and version vectors.
