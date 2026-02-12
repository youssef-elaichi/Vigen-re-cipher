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
def encrypt(text, key): # We define the encrypt function that takes the text and the key as parameters
    text = text.upper() # We change the text to uppercase to simplify the encryption process
    key = repeat_key(text, key.upper()) # We repeat the key to match the length of the text
    ciphertext = ""

    for t_char, k_char in zip(text, key): # We iterate through the text and the repeated key simultaneously using the zip function
        if t_char.isalpha(): # We check if the character is an alphabet
            t_num = ord(t_char) - ord('A') # We convert the character to a number between 0 and 26 by subtracting the ASCII value of 'A' from the ASCII value of the character
            k_num = ord(k_char) - ord('A') # We do the same for the key character
            c_num = (t_num + k_num) % 26 # We add the text number and the key number and taket the modulus 26 to wrap around the alphabet
            c_char = chr(c_num + ord('A')) # We convert the resulting number back to a character by adding the ASCII value of 'A'
            ciphertext += c_char
        else:
            ciphertext += t_char
    return ciphertext
def decrypt(ciphertext, key): # We define the decrypt function that takes the ciphertext and the key as parameters
    ciphertext = ciphertext.upper() # We change the ciphertext to uppercase to simplify the decryption process
    key =repeat_key(ciphertext, key.upper())
    plaintext = ""
    for c_char, k_char in zip(ciphertext, key):
        if c_char.isalpha():
            c_num = ord(c_char) - ord('A')
            k_num = ord(k_char) - ord('A')
            t_num = (c_num - k_num + 26) % 26 # We subtract the key number from the ciphertext number and add 26 to ensure we get a positive result before taking modulus 26
            t_char = chr(t_num + ord('A'))
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

