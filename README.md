# 🔴 SocketShell

**SocketShell** is a Python-based TCP client-server communication project designed to demonstrate how two systems can establish a connection and exchange messages using socket programming.

The project demonstrates fundamental concepts used in **networking and Red Team cybersecurity labs**, including TCP connections, client-server architecture, message transmission, and interactive command-line communication.

> ⚠️ **Educational Use Only:** This project is intended for authorized cybersecurity labs, personal testing environments, and educational purposes. Do not use it against systems or networks without explicit permission.

---

## 📌 Features

- TCP socket communication
- Client-server architecture
- Interactive command-line interface
- Bidirectional message exchange
- Configurable server IP and port
- Connection termination using `q`
- Built using Python's standard `socket` library
- Simple implementation for learning networking fundamentals

---

## 🏗️ Project Structure

```text
SocketShell/
│
├── server.py       # Server-side socket
├── rat.py          # Client-side socket
└── README.md       # Project documentation
```

---

## 🔄 How It Works

SocketShell consists of two components:

### 🖥️ Server

The server creates a TCP socket, binds it to an IP address and port, listens for connections, and accepts a client connection.

Once connected, the server can send messages and receive responses from the client.

### 💻 Client

The client creates a TCP socket and connects to the configured server address.

After establishing the connection, it receives messages from the server and allows the user to send a response back.

### Communication Flow

```text
        ┌─────────────────┐
        │      Server     │
        │    server.py    │
        └────────┬────────┘
                 │
                 │ TCP Connection
                 │
                 ▼
        ┌─────────────────┐
        │      Client     │
        │     rat.py      │
        └─────────────────┘

        Server  ────────►  Client
        Server  ◄────────  Client
```

---

## ⚙️ Requirements

- Python 3.x
- Two systems on the same network **or** a suitable authorized test environment
- Network connectivity between the client and server

No external Python packages are required.

---

## 🚀 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/SocketShell.git
cd SocketShell
```

### 2. Configure the Server

Open `server.py` and configure the IP address and port:

```python
s.bind(("YOUR_SERVER_IP", 1111))
```

The current implementation uses TCP port `1111`.

### 3. Configure the Client

Open the client script and configure it with the server's IP address and port:

```python
sock.connect(("YOUR_SERVER_IP", 1111))
```

The client then establishes the TCP connection to the server.

---

## ▶️ Running the Project

### Start the Server First

```bash
python server.py
```

You should see:

```text
Listening for Incoming connection
```

The server waits for an incoming client connection.

### Start the Client

On the client machine:

```bash
python rat.py
```

After the connection is established:

```text
Connection Established To Server
```

The client then waits for messages from the server.

---

## 💬 Message Communication

The server can enter a message through the command-line interface:

```text
*shell#~('CLIENT_IP', PORT):Hello
```

The client receives the message and can respond:

```text
Type Message To Send To Server: Hello Server
```

The client sends the response back through the TCP socket.

The server receives and displays the response.

---

## 🛑 Closing the Connection

The project uses:

```text
q
```

as the termination message.

When `q` is sent, the communication loop exits and the socket is closed.

---

## 🧠 Concepts Demonstrated

This project is useful for learning:

- **TCP/IP**
- **Socket Programming**
- **Client-Server Architecture**
- **IP Addresses**
- **TCP Ports**
- **Connection Establishment**
- **Data Transmission**
- **Message Encoding/Decoding**
- **Interactive Network Communication**
- **Basic Red Team Networking Concepts**

---

## 🔐 Cybersecurity Context

SocketShell is a small educational implementation that helps demonstrate the networking principles behind remote communication tools.

It can be used in an isolated cybersecurity lab to understand how a TCP connection is established and how data can be exchanged between a server and client.

It does **not** implement persistence, privilege escalation, credential theft, or stealth mechanisms.

---

## ⚠️ Disclaimer

This project is created strictly for **educational and authorized security-testing purposes**.

Only run SocketShell on:

- Systems you own
- Your own virtual machines
- Authorized penetration-testing environments
- Cybersecurity training labs such as CTF environments

**Do not use this project to access, control, or communicate with systems without explicit authorization.**

---

## 👨‍💻 Author

**Sahil Chauhan**

Cybersecurity / Red Team Learning Project

---

## ⭐ Future Improvements

Possible future learning extensions include:

- Improved error handling
- Connection status handling
- Multiple client support
- Message timestamps
- Better command-line interface
- Secure communication using TLS
- Authentication
- Logging
- Structured message protocol

---

## 📜 License

This project is provided for educational and research purposes. Use responsibly and only in environments where you have permission.
