from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# pip install pycryptodome

key = input("Enter 8-character key: ").encode()
plaintext = input("Enter plaintext: ").encode()

if len(key) != 8:
    print("Key must be exactly 8 characters.")
else:
    cipher = DES.new(key, DES.MODE_ECB)

    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

    print("\nPlaintext :", plaintext.decode())
    print("Key       :", key.decode())
    print("Ciphertext:", ciphertext.hex())

    decrypted = cipher.decrypt(ciphertext)
    decrypted = unpad(decrypted, DES.block_size)

    print("Decrypted :", decrypted.decode())
