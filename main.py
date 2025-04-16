# main.py

import os
from port_scanner import run_port_scanner
from pass_r import check_password_strength

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear()

        print("┌─[ Toolkit for Engineers ]")
        print("│  1. Port Scanner")
        print("│  2. Check Password Strength")
        print("│  0. Exit")
        print("└─ Choose an option:")
        
        choice = input("shell_$~ ").strip()

        if choice == '1':

            run_port_scanner()

        elif choice == '2':

            password = input("Enter password to check: ")

            check_password_strength(password)

            input("\nPress Enter to Continue...")

        elif choice == '0':

            print("\n[+] Exiting... Stay safe, bruv 😎")
            break

        else:
            
            print("\n[!] Invalid option.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()