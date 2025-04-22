# combo_generator.py

import itertools
import string

def generate_all_combos(charset, max_length):
    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            yield ''.join(combo)

def run_combo_generator():
    print("\n=== Full Password Combo Generator ===")
    
    print("Choose character sets:")
    print("1. lowercase letters")
    print("2. digits")
    print("3. symbols")
    print("4. uppercase letters")
    
    choices = input("Enter options (e.g., 123): ")
    charset = ''
    
    if '1' in choices:
        charset += string.ascii_lowercase
    if '2' in choices:
        charset += string.digits
    if '3' in choices:
        charset += string.punctuation
    if '4' in choices:
        charset += string.ascii_uppercase

    if not charset:
        print("No valid character sets selected.")
        input("Press Enter to return...")
        return
    
    try:
        max_len = int(input("Max password length (e.g., 4): "))
    except ValueError:
        print("Invalid length.")
        input("Press Enter to return...")
        return

    filename = input("Output filename (e.g., combos.txt): ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for password in generate_all_combos(charset, max_len):
                f.write(password + '\n')
        print(f"\n✅ Saved all combos to {filename}")
    except Exception as e:
        print(f"❌ Error writing to file: {e}")

    input("\nPress Enter to return to main menu...")
