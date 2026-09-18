import numpy as np


def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]


def numbers_to_text(numbers):
    return ''.join(chr(int(n) + ord('A')) for n in numbers)


def encrypt(plaintext, key):
    numbers = text_to_numbers(plaintext)

    n = len(key)

    # Add X until length becomes a multiple of matrix size
    while len(numbers) % n != 0:
        numbers.append(23)

    ciphertext = ""

    for i in range(0, len(numbers), n):
        p = np.array(numbers[i:i+n]).reshape(n, 1)

        c = np.dot(key, p) % 26

        ciphertext += numbers_to_text(c.flatten())

    return ciphertext


def decrypt(ciphertext, key):
    n = len(key)

    # Find determinant 
    det = int(round(np.linalg.det(key))) % 26

    # Find modular inverse of determinant
    det_inv = pow(det, -1, 26)

    # Find inverse matrix using adjugate
    inverse_key = np.linalg.inv(key) * det

    inverse_key = np.round(inverse_key).astype(int)

    inverse_key = (det_inv * inverse_key) % 26

    numbers = text_to_numbers(ciphertext)

    plaintext = ""

    for i in range(0, len(numbers), n):
        c = np.array(numbers[i:i+n]).reshape(n, 1)

        p = np.dot(inverse_key, c) % 26

        plaintext += numbers_to_text(p.flatten())

    return plaintext


# ---------------- MAIN PROGRAM ----------------

plaintext = input("Enter plaintext: ")

# Matrix size
n = int(input("Enter size of key matrix (e.g., 2 or 3): "))

# Take key matrix from user
print("Enter the key matrix:")

key = []

for i in range(n):
    row = []

    for j in range(n):
        value = int(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(value)

    key.append(row)

key = np.array(key)

# Encryption
ciphertext = encrypt(plaintext, key)

# Decryption
decryptedtext = decrypt(ciphertext, key)

print("\nPlaintext :", plaintext)

print("Key Matrix:")
print(key)

print("\nCipher text: ",ciphertext)
print("Decrypted text: ", decryptedtext)

