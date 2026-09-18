def encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char.isalpha():
            p = ord(char) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')

            c = (p + k) % 26
            result += chr(c + ord('A'))

            key_index += 1
        else:
            result += char

    return result


def decrypt(ciphertext, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')

            p = (c - k) % 26
            result += chr(p + ord('A'))

            key_index += 1
        else:
            result += char

    return result


# Main program
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)
