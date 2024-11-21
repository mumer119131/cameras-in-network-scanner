# Network Camera Scanner

A Python tool to scan a local network for devices that may be cameras. The script scans a specified network range for devices with open ports commonly used by cameras, such as 80, 8080, 554, 8554, and 10554.

## Features
- Automatically detects the default gateway and network range.
- Scans for devices with open ports commonly associated with cameras.
- Multi-threaded scanning for fast results.
- Customizable network range and port selection.

## Prerequisites
- Python 3.8 or higher.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mumer119131/network-camera-scanner.git
   cd network-camera-scanner
   ```

## Usage

    ```bash
    python scanner.py
    `

```# FAQ - Network Camera Scanner

### 1. What does this tool do?
The Network Camera Scanner scans a local network for devices with open ports commonly associated with cameras, such as ports 80, 8080, 554, 8554, and 10554.

---

### 2. What do I need to run this tool?
You need:
- Python 3.8 or higher.
- A computer connected to the same network as the devices you want to scan.

---

### 3. How does the tool determine the network range?
The tool automatically detects the default gateway and subnet mask of your system using system commands like `ipconfig` (Windows) or `ip route` (Linux/macOS). From this information, it constructs the default network range.

---

### 4. Can I specify a custom network range?
Yes! The tool will prompt you to confirm or override the detected network range. You can enter a custom range in CIDR notation, like `192.168.1.0/24`.

---

### 5. What ports are scanned by default?
The default ports scanned are:
- **80** (HTTP)
- **8080** (Alternate HTTP)
- **554** (RTSP)
- **8554** (RTSP alternate)
- **10554** (RTSP alternate)

You can customize this list by editing the `camera_ports` variable in the `scanner.py` file.

---

### 6. How long does the scan take?
The duration depends on:
- The size of the network range (e.g., `/24` scans 256 addresses).
- The number of ports being scanned.
- Your system's performance and network speed.

The script uses multi-threading to improve scan speed.

---

### 7. Can this tool detect if a device is actually a camera?
No. The tool only checks for open ports commonly associated with cameras. It does not verify if the device is a camera.

---

### 8. What should I do if the tool doesn’t detect my network range?
Ensure your system has an active network connection. If the issue persists:
- On Windows, check the output of `ipconfig` in your terminal.
- On Linux/macOS, check the output of `ip route`.

If necessary, enter the network range manually when prompted.

---

### 9. Is it safe to use this tool?
This tool performs network scans, which may trigger alerts on some networks. Ensure you have permission to scan the network before using this tool.

---

### 10. Can I contribute to this project?
Absolutely! Contributions, bug reports, and feature suggestions are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

---

### 11. How do I report a bug or request a feature?
You can open an issue on the GitHub repository. Please provide a detailed description of the problem or feature request.

---

### 12. What if I encounter a permission error?
Running the tool typically does not require elevated privileges. However, if you experience permission-related issues, ensure you are using a user account with sufficient network access rights.

---

### 13. Can this tool scan external or public networks?
No. This tool is designed for local network scanning only. Scanning external or public networks may violate legal and ethical guidelines.

---

### 14. What license does this project use?
The project is licensed under the MIT License. See the `LICENSE` file for details.

---

### 15. Where can I learn more about how this tool works?
Refer to the [README.md](README.md) file in the repository for detailed information about the tool’s features, installation, and usage.


## Authors

- [@mumer119131](https://www.github.com/mumer119131)

