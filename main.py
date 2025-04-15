# main.py

import os
from port_scanner import run_port_scanner

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear()
        print("┌─[ Vulnerability Detector ]")
        print("│  1. Port Scanner")
        print("│  0. Exit")
        print("└─ Choose an option:")
        
        choice = input("shell_$~ ").strip()

        if choice == '1':
            run_port_scanner()
        elif choice == '0':
            print("\n[+] Exiting... Stay safe, hacker 😎")
            break
        else:
            print("\n[!] Invalid option.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()