from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# Generate a 128-bit key and a 128-bit IV
key = os.urandom(16)
iv = os.urandom(16)

# Input plaintext
plaintext = input("Enter plaintext: ").encode()

# Apply PKCS7 padding
padder = padding.PKCS7(128).padder()
padded_data = padder.update(plaintext) + padder.finalize()

# AES Encryption
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

print("Encrypted text:", ciphertext.hex())

# AES Decryption
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

# Remove padding
unpadder = padding.PKCS7(128).unpadder()
decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

print("Decrypted text:", decrypted.decode())
