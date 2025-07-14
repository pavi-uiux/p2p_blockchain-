# 🚀 P2P Blockchain Network Simulation

This project simulates a peer-to-peer (P2P) blockchain network using Python, Flask, and a simple web interface.

## 📚 Assignment Objective

> Help students understand the inner workings of blockchain by simulating multiple nodes that maintain independent blockchain copies and communicate to sync blocks.

## ✅ Technologies Used

- Python 3.x
- Flask
- Requests (for HTTP between nodes)
- Bootstrap 5 (for frontend)

---

## ✅ Features

✅ Simple blockchain structure:
- Transactions
- Blocks
- Entire chain

✅ Mining logic with Proof-of-Work (PoW):
- New blocks require valid proof
- Uses simple hash puzzle (leading zeros)

✅ Multiple nodes:
- Run separate nodes on different ports
- Each node has its own blockchain

✅ Node discovery:
- Nodes can register other nodes

✅ Consensus algorithm:
- Longest valid chain wins

✅ Blockchain sync:
- Nodes adopt longer valid chains from peers

✅ Professional web UI:
- Add transactions
- Mine blocks
- Register nodes
- Resolve conflicts
- Visual blockchain visualization

---

## ✅ How to Run This Project

### 1. Install dependencies

```bash
pip install flask requests
```

---

### 2. Run Node

Start your first node on port 5000:

```bash
python run_node.py 5000
```

Start additional nodes on other ports:

```bash
python run_node.py 5001
python run_node.py 5002
```

---

### 3. Open Web Interface

Open your browser:

```
http://127.0.0.1:5000
```

---

## ✅ How to Use

### ➕ Add Transaction

- Fill out **Sender**, **Recipient**, **Amount**
- Click **Submit Transaction**

---

### 🔨 Mine Block

- Click **Mine Block**
- Adds pending transactions into a new block

---

### 🔗 Register Nodes

- Enter other node addresses like:
  
  ```
  127.0.0.1:5001,127.0.0.1:5002
  ```

- Click **Register Nodes**

---

### ⚖️ Resolve Conflicts

- Click **Resolve Conflicts**
- Node fetches chains from peers
- Adopts longest valid chain if found

---

### 👀 View Blockchain

- Scroll down to see **block cards** in the web UI
- Or access JSON chain:

```
http://127.0.0.1:5000/chain
``
