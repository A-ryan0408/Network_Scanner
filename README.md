# Network_Scanner
Python-based tool probing a network, swiftly identifying devices' IP &amp; MAC addresses. Aids in network mapping and security by swiftly cataloging connected devices for analysis.

Certainly! Here's a README file providing usage instructions for the network scanner script and suggestions for compatibility:

---

# Network Scanner

## Overview

This Python script utilizes the `scapy` library to perform network scanning. It discovers devices within a specified IP range, capturing their IP and MAC addresses. This tool aids in network analysis and security assessment by identifying connected devices.

## Usage

1. **Dependencies**:
   - Ensure you have Python installed.
   - Install `scapy` via `pip install scapy`.

2. **Running the Script**:
   - Modify `target_ip_range` variable in the script to define the IP range you want to scan.
   - Execute the script (`python network_scanner.py`).
   - The script sends ARP requests to the specified IP range, capturing IP and MAC addresses of active devices.

3. **Viewing Results**:
   - The script will display the discovered IP and MAC addresses of devices within the specified range.

---
