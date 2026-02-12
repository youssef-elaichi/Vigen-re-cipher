def repeat_key(text, key): # We define the repeat_key function that takes the text and the key as parameters
    repeated_key = "" # We initialize an empty string to store the repeated key
    key_index = 0 # We initialize a key index to keep track of our position in the key
    for char in text: # We iterate through each character in the text 
        if char.isalpha(): # We check if the character is an alphabet
            repeated_key += key[key_index % len(key)] # We repeat the key by using the modulus operator to wrap around the key
            key_index += 1 # We increment the key index to move to the next character in the key
        else:
            repeated_key += char # It is not an alphabet, so we keep it as it is 
    return repeated_key

def encrypt(text, key):
    key = repeat_key(text, key)  # ما كنحولوش للـ upper هنا
    ciphertext = ""

    for t_char, k_char in zip(text, key):
        if t_char.isupper():  # حرف كبير
            t_num = ord(t_char) - ord('A')
            k_num = ord(k_char.upper()) - ord('A')
            c_num = (t_num + k_num) % 26
            c_char = chr(c_num + ord('A'))
            ciphertext += c_char
        elif t_char.islower():  # حرف صغير
            t_num = ord(t_char) - ord('a')
            k_num = ord(k_char.lower()) - ord('a')
            c_num = (t_num + k_num) % 26
            c_char = chr(c_num + ord('a'))
            ciphertext += c_char
        else:  
            ciphertext += t_char

    return ciphertext

def decrypt(ciphertext, key):
    key = repeat_key(ciphertext, key)
    plaintext = ""

    for c_char, k_char in zip(ciphertext, key):
        if c_char.isupper():
            c_num = ord(c_char) - ord('A')
            k_num = ord(k_char.upper()) - ord('A')
            t_num = (c_num - k_num + 26) % 26
            t_char = chr(t_num + ord('A'))
            plaintext += t_char
        elif c_char.islower():
            c_num = ord(c_char) - ord('a')
            k_num = ord(k_char.lower()) - ord('a')
            t_num = (c_num - k_num + 26) % 26
            t_char = chr(t_num + ord('a'))
            plaintext += t_char
        else:
            plaintext += c_char

    return plaintext

# Example usage
# =============================
# the main program
# =============================
print("=== Vigenere Cipher ===")
while True:

    print("\n1 - Encrypt")
    print("2 - Decrypt")
    print("3 - Exit")

    choice = input(" Choose an option (1/2/3): ")


    if choice not in ['1', '2', '3']:
        print("Invalid option. Please choose 1, 2, or 3.")
        continue

    if choice == '1':
        text = input("Enter the text to encrypt: ")

        while True:
            key = input("Enter the key: ")
            if key.isalpha():
                break
            print("Key must contain only letters!")


        cipher_text = encrypt(text, key)
        print(f"Encrypted text: {cipher_text}")

    elif choice == '2':
        text = input("Enter the text to decrypt: ")

        while True:
            key = input("Enter the key: ")
            if key.isalpha():
                break
            print("Key must contain only letters!")

        original_text = decrypt(text, key)
        print(f"Decrypted text: {original_text}")

        
    elif choice == "3":
        print("Goodbye 👋")
        break

