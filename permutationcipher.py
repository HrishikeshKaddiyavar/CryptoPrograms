# permutation cipher

def encrypt(text, key):
    result = ""

    for i in range(0, len(text), len(key)):
        block = text[i:i + len(key)]

        if len(block) < len(key):
            block += 'X' * (len(key) - len(block))

        for position in key:
            result += block[position - 1]

    return result


def decrypt(text, key):
    result = ""

    for i in range(0, len(text), len(key)):
        block = text[i:i + len(key)]
        original = [''] * len(key)

        for j in range(len(key)):
            original[key[j] - 1] = block[j]

        result += ''.join(original)

    return result


plaintext = input("Enter plaintext: ")
key = list(map(int, input("Enter permutation key: ").split()))

ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

print("\nPlaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)
