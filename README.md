# CodeAlpha_NetworkSniffer
A Python-based network sniffer built using Scapy to capture and analyze live network packets, displaying IP addresses, protocols, and payload data for cybersecurity learning.

# 🛡️ Basic Network Sniffer (CodeAlpha Internship)

## 📌 Project Overview
This project is part of the CodeAlpha Cyber Security Internship.

The objective is to build a basic network sniffer using Python that captures and analyzes network traffic in real-time. The program extracts useful information such as source and destination IP addresses, protocols, and packet payloads.

---

## ⚙️ Technologies Used
- Python
- Scapy (Packet Manipulation Library)

---

## 🚀 Features
- Capture live network packets
- Display source and destination IP addresses
- Identify protocols (TCP, UDP, Others)
- Extract and display payload data
- Real-time packet analysis

---

## 🧠 How It Works
The script uses the Scapy library to sniff packets from the network interface.  
Each captured packet is analyzed to extract:

- IP Layer information
- Protocol type (TCP/UDP)
- Raw payload data (if available)

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install scapy
