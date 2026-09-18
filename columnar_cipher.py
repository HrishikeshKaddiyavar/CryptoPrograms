def encrypt(plain_text, key):
    n = len(key)
    table = [[] for i in key]

    j = 0
    for i in plain_text:
        j = j%n
        table[j].append(i)
        j+=1

    while j<n:
        j = j%n
        table[j].append('_')
        j+=1

    cipher_text = ""
    for index, value in sorted(enumerate(key), key=lambda x: x[1]):
        cipher_text+="".join(table[index])

    return cipher_text


def decrypt(cipher_text, key):
    n = len(key)

    rows = len(cipher_text) // n
    order = sorted(range(n), key=lambda i: key[i])
    table = [None] * n
    start = 0
    for index in order:
        table[index] = cipher_text[start:start + rows]
        start += rows
    plain_text = ""
    for row in range(rows):
        for col in range(n):
            plain_text += table[col][row]
    return plain_text.rstrip("_")

plain_text = "Geeks for Geeks"
key = "3124"

cipher_text = encrypt(plain_text, key)

print("Plain text :", plain_text)
print("Cipher text:", cipher_text)

decrypted = decrypt(cipher_text, key)

print("Decrypted  :", decrypted)

