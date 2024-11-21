import os
import re
import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def get_default_gateway():
    """
    Retrieves the default gateway from the system's network configuration.
    Works for Windows, Linux, and macOS.
    """
    try:
        if os.name == 'nt':  # Windows
            output = os.popen('ipconfig').read()
            match = re.search(r"Default Gateway(?:\.|\s)*:\s*([\d\.]+)", output)
        else:  # Linux/macOS
            output = os.popen('ip route').read()
            match = re.search(r'default via ([\d.]+)', output)
            
        print(f"Detected default gateway: {match.group(1)}")
        if match:
            gateway = match.group(1)
            if re.match(r'^\d+\.\d+\.\d+\.\d+$', gateway):  # Validate IP format
                return f"{gateway.rsplit('.', 1)[0]}.0/24"
    except Exception as e:
        print(f"Error detecting default gateway: {e}")
    return None

def is_camera(ip, ports):
    """
    Checks if the given IP has an open port commonly used by cameras.
    """
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Timeout for responsiveness
                result = s.connect_ex((ip, port))
                if result == 0:
                    print(f"[+] Potential camera found: {ip}:{port}")
                    return True
        except Exception as e:
            pass
    return False

def scan_network(network, ports, threads=50):
    """
    Scans the specified network for devices with open ports.
    """
    print(f"Scanning network {network} for cameras on ports: {ports}")
    potential_cameras = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(is_camera, str(ip), ports): ip for ip in ipaddress.IPv4Network(network, strict=False)}
        for future in futures:
            ip = futures[future]
            if future.result():
                potential_cameras.append(ip)
    return potential_cameras

if __name__ == "__main__":
    # Try to get the default gateway
    default_network_range = get_default_gateway()
    if default_network_range:
        print(f"Default network detected: {default_network_range}")
    else:
        print("Default gateway not detected. Using fallback.")
        default_network_range = "192.168.1.0/24"  # Fallback to a common subnet
    
    # Allow the user to override the detected range
    network_range = input(f"Enter the network range (default: {default_network_range}): ") or default_network_range
    camera_ports = [80, 8080, 554, 8554, 10554]  # Common camera ports
    found_cameras = scan_network(network_range, camera_ports)

    if found_cameras:
        print("\nDiscovered Cameras:")
        print("\nIP Address")
        print("-" * 15)
        for camera in found_cameras:
            print(camera)
    else:
        print("No cameras found on the network.")
