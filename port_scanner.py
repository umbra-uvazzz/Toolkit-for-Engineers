# port_scanner.py

import socket
import threading
from datetime import datetime

# Store open ports
open_ports = []

def scan_port(ip: str, port: int):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)
    except Exception:
        pass

def run_port_scanner():
    target = input("Target IP or Hostname: ").strip()

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[ERROR] Unable to resolve host.")
        return

    print(f"\n[+] Scanning {target_ip} (Ports 1–1024)...\n")
    start_time = datetime.now()

    threads = [
        threading.Thread(target=scan_port, args=(target_ip, port))
        for port in range(1, 1025)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    duration = datetime.now() - start_time
    print(f"\n[✓] Scan completed in {duration}")
    print(f"[+] Open Ports: {sorted(open_ports) if open_ports else 'None found'}")

    input("\nPress Enter to return to main menu...")