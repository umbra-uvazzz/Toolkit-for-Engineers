import itertools
import string
import time
import threading

CHARSET = string.ascii_letters + string.digits + string.punctuation


found = False
lock = threading.Lock()
attempts = 0

def brute_force_worker(password, length):
    global found, attempts

    for guess in itertools.product(CHARSET, repeat=length):
        if found:
            return

        guess_str = ''.join(guess)

        with lock:
            attempts += 1

        if guess_str == password:
            with lock:
                found = True
                duration = time.time() - start_time
                print(f"\n✅ Password '{password}' cracked in {attempts} attempts!")
                print(f"⏱️ Time taken: {duration:.2f} seconds")
            return

def brute_force_simulation(password, max_length=None, num_threads=8):
    global found, start_time, attempts
    found = False
    attempts = 0

    max_length = max_length or len(password) + 2
    start_time = time.time()

    print(f"\n[!] Brute-forcing password: {password}")
    print(f"[+] Character set: {len(CHARSET)} characters")
    print(f"[+] Max length: {max_length}\n")

    for length in range(1, max_length + 1):
        if found:
            break

        threads = []
        combos = list(itertools.product(CHARSET, repeat=length))
        chunk_size = len(combos) // num_threads + 1

        for i in range(num_threads):
            chunk = combos[i*chunk_size:(i+1)*chunk_size]
            t = threading.Thread(target=check_combos, args=(password, chunk))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    if not found:
        print("\n❌ Password not cracked.")

def check_combos(password, combo_chunk):
    global found, attempts
    for guess in combo_chunk:
        if found:
            return

        guess_str = ''.join(guess)

        with lock:
            attempts += 1

        if guess_str == password:
            with lock:
                found = True
                duration = time.time() - start_time
                print(f"\n✅ Password '{password}' cracked in {attempts} attempts!")
                print(f"⏱️ Time taken: {duration:.2f} seconds")
            return

if __name__ == "__main__":
    pwd = input("Enter a password (simple for demo, like 'a1B@'): ")
    brute_force_simulation(pwd)