def leetspeak(word):
    substitutions = {
        'a': '@', 's': '$', 'i': '1', 'o': '0', 'e': '3', 'l': '1'
    }
    return ''.join(substitutions.get(c.lower(), c) for c in word)

def generate_variants(base):
    base = base.lower()
    variants = set()

    variants.update([
        base,
        base.capitalize(),
        base.upper(),
        base + '123',
        base + '!',
        base + '@',
        base[::-1],
        leetspeak(base),
        base + '2023',
        base + '2024',
        leetspeak(base + '123'),
        leetspeak(base[::-1]),
    ])

    return variants

def main():
    print("=== Custom Wordlist Generator ===")
    base_words = input("Enter keywords (comma-separated): ").split(',')

    wordlist = set()
    for word in base_words:
        word = word.strip()
        if word:
            wordlist.update(generate_variants(word))

    filename = input("Enter output filename (e.g., mywordlist.txt): ").strip()
    if not filename.endswith('.txt'):
        filename += '.txt'

    with open(filename, 'w', encoding='utf-8') as f:
        for word in wordlist:
            f.write(word + '\n')

    print(f"\n✅ Wordlist saved as '{filename}' with {len(wordlist)} entries.")

if __name__ == "__main__":
    main()
