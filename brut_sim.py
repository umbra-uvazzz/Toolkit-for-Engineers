import itertools
import string
import time
import threading

CHARSET = string.ascii_letters + string.digits + string.punctuation
found = False
attempts = 0
lock = threading.Lock()

def scan_password(password, max_length=5, num_threads=8):
    global found, attempts
    found = False
    attempts = 0
    start_time = time.time()

    print(f"\n[!] Brute-forcing: {password}")

    for length in range(1, max_length + 1):
        if found:
            break

        generator = itertools.product(CHARSET, repeat=length)

        threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=worker, args=(password, generator))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    if not found:
        print("\n❌ Could not crack the password.")
    else:
        duration = time.time() - start_time
        print(f"\n✅ Cracked in {attempts} attempts!")
        print(f"⏱️ Time taken: {duration:.2f} seconds")

def worker(password, generator):
    global found, attempts
    while not found:
        with lock:
            try:
                guess = next(generator)
            except StopIteration:
                break

        guess_str = ''.join(guess)
        with lock:
            attempts += 1

        if guess_str == password:
            with lock:
                found = True
                print(f"\n🚨 MATCH FOUND: {guess_str}")
            return

if __name__ == "__main__":
    pwd = input("Enter a password (short for demo): ")
    scan_password(pwd, max_length=len(pwd) + 1)
