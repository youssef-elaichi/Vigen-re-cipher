def repeat_key(text, key):
    pepeated_key = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            pepeated_key = key[key_index % len(key)]

