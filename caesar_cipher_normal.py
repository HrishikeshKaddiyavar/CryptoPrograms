def encrypt(text, shift):
    result = ""

    for c in text:
        if 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += c

    return result


def decrypt(text, shift):
    result = ""

    for c in text:
        if 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += c

    return result


plain_text = input("Enter plaintext: ")
shift = int(input("Enter shift: "))
plain_text = plain_text.upper()

encrypted_text = encrypt(plain_text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
