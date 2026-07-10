# 🚀 Distributed Key-Value Store

A multithreaded TCP-based Distributed Key-Value Store developed using Python. The server supports multiple concurrent clients, provides thread-safe operations, and persists data using JSON storage.

---

# 📌 Features

- Multi-client TCP Server
- Concurrent Client Handling using Threads
- Thread-safe Database using `threading.Lock`
- JSON Persistent Storage
- Client-Server Architecture
- Command-Based Protocol
- Fast Key-Value Operations

---

# 🛠 Tech Stack

- Python 3
- Socket Programming
- Multithreading
- JSON
- Git
- Ubuntu (WSL2)

---

# 📂 Project Structure

```
distributed-key-value-store/

│── server.py
│── client.py
│── storage.py
│── config.py
│── requirements.txt
│── README.md
│── .gitignore

├── data/
│      database.json

├── screenshots/

└── venv/
```

---

# ⚙️ Installation

Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/distributed-key-value-store.git
```

Go inside

```bash
cd distributed-key-value-store
```

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate

Linux / WSL

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Start the server

```bash
python3 server.py
```

Open another terminal

```bash
python3 client.py
```

---

# 💻 Available Commands

| Command | Description |
|----------|-------------|
| SET key value | Store a key-value pair |
| GET key | Retrieve value |
| DELETE key | Delete key |
| KEYS | Display all keys |
| COUNT | Number of stored keys |
| EXIT | Disconnect client |

---

# 📸 Example

Client

```
SET name Rohit
OK

SET college RSCOE
OK

GET name
Rohit

GET college
RSCOE

COUNT
2

KEYS
name, college

DELETE name
Deleted
```

---

# 🏗 Architecture

```
            Client 1
                │
                │
           TCP Socket
                │
      +----------------+
      |                |
      |   Server.py    |
      |                |
      +----------------+
           │       │
           │       │
   Thread-1    Thread-2
           │       │
        Shared Dictionary
               │
        threading.Lock
               │
        database.json
```

---

# 🔒 Thread Safety

The project uses Python's `threading.Lock()` to synchronize write operations and prevent race conditions when multiple clients access the shared in-memory database simultaneously.

---

# 💾 Persistent Storage

All key-value pairs are automatically stored in

```
data/database.json
```

This allows data recovery after restarting the server.

---

# 🎯 Learning Outcomes

This project helped me understand:

- TCP Socket Programming
- Client-Server Communication
- Multithreading
- Synchronization
- Thread Safety
- JSON File Handling
- Persistent Storage
- Concurrent Programming
- Distributed Systems Fundamentals

---

# 🚀 Future Improvements

- Authentication
- Logging
- Docker Deployment
- REST API
- Replication
- Distributed Cluster
- Redis Protocol Support

---

# 👨‍💻 Author

**Rohit Mahargude**

GitHub

https://github.com/YOUR_USERNAME
