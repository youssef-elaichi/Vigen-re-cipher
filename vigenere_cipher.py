# ==============================
# Project: Vigenere Cipher
# Goal: Encrypt and decrypt text using Vigenere cipher
# Supports both manual input and reading/writing files
# Preserves letter case and ignores non-alphabetic characters
# ==============================
import time  

def repeat_key(text, key):
    """Repeat the key to match the length of the text, skipping non-alphabetic characters."""
    repeated_key = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            repeated_key += key[key_index % len(key)]
            key_index += 1
        else:
            repeated_key += char
    return repeated_key


def encrypt_with_progress(text, key):
    key = repeat_key(text, key)
    ciphertext = ""

    for i, (t_char, k_char) in enumerate(zip(text, key), start=1):

        if t_char.isupper():
            t_num = ord(t_char) - ord('A')
            k_num = ord(k_char.upper()) - ord('A')
            c_num = (t_num + k_num) % 26
            ciphertext += chr(c_num + ord('A'))
        elif t_char.islower():
            t_num = ord(t_char) - ord('a')
            k_num = ord(k_char.lower()) - ord('a')
            c_num = (t_num + k_num) % 26
            ciphertext += chr(c_num + ord('a'))
        else:
            ciphertext += t_char

        # Print progress every 5%
        if i % max(1, len(text)//20) == 0:
            percent = (i / len(text)) * 100
            print(f"Progress: {percent:.0f}%", end="\r")
            time.sleep(0.01)  # Optional: slow down to see progress

    print()  # new line after progress
    return ciphertext


def decrypt_with_progress(ciphertext, key):
    """Decrypt the text with progress feedback."""
    key = repeat_key(ciphertext, key)
    plaintext = ""

    for i, (c_char, k_char) in enumerate(zip(ciphertext, key), start=1):
        if c_char.isupper():
            c_num = ord(c_char) - ord('A')
            k_num = ord(k_char.upper()) - ord('A')
            t_num = (c_num - k_num + 26) % 26
            plaintext += chr(t_num + ord('A'))
        elif c_char.islower():
            c_num = ord(c_char) - ord('a')
            k_num = ord(k_char.lower()) - ord('a')
            t_num = (c_num - k_num + 26) % 26
            plaintext += chr(t_num + ord('a'))
        else:
            plaintext += c_char

        # Print progress every 5%
        if i % max(1, len(ciphertext)//20) == 0:
            percent = (i / len(ciphertext)) * 100
            print(f"Progress: {percent:.0f}%", end="\r")
            time.sleep(0.01)  # Optional: slow down to see progress

    print()  # new line after progress
    return plaintext


# ==============================
# Main Program with Menu
# ==============================
print("=== Vigenere Cipher ===")

while True:
    print("\n1 - Encrypt")
    print("2 - Decrypt")
    print("3 - Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice not in ['1', '2', '3']:
        print("Invalid option. Please choose 1, 2, or 3.")
        continue

    if choice == '1':
        mode = input("Encrypt from file (1) or manual input (2)? Choose 1/2: ")
        while mode not in ['1', '2']:
            mode = input("Invalid choice! Choose 1 for file, 2 for manual input: ")

        if mode == '1':  # Read from file
            try:
                with open("input.txt", "r", encoding="utf-8") as f:
                    text = f.read()
            except FileNotFoundError:
                print("File input.txt not found!")
                continue
        else:
            text = input("Enter the text to encrypt: ")

        # Validate key
        while True:
            key = input("Enter the key: ")
            if key.isalpha():
                break
            print("Key must contain only letters!")

        # Encrypt text
        cipher_text = encrypt_with_progress(text, key)
        print(f"Encrypted text:\n{cipher_text}")

        # Write to file
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(cipher_text)
        print("Encrypted text saved to output.txt")

    elif choice == '2':
        mode = input("Decrypt from file (1) or manual input (2)? Choose 1/2: ")
        while mode not in ['1', '2']:
            mode = input("Invalid choice! Choose 1 for file, 2 for manual input: ")

        if mode == '1':  # Read from file
            try:
                with open("input.txt", "r", encoding="utf-8") as f:
                    text = f.read()
            except FileNotFoundError:
                print("File input.txt not found!")
                continue
        else:
            text = input("Enter the text to decrypt: ")

        # Validate key
        while True:
            key = input("Enter the key: ")
            if key.isalpha():
                break
            print("Key must contain only letters!")

        # Decrypt text
        original_text = decrypt_with_progress(text, key)
        print(f"Decrypted text:\n{original_text}")

        # Write to file
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(original_text)
        print("Decrypted text saved to output.txt")

    elif choice == '3':
        print("Goodbye 👋")
        break
