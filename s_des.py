# Simplified DES (S-DES)

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [[1, 0, 3, 2], [3, 2, 1, 0],
      [0, 2, 1, 3], [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3], [2, 0, 1, 3],
      [3, 0, 1, 0], [2, 1, 0, 3]]


def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)


def shift(bits, n):
    return bits[n:] + bits[:n]


def xor(a, b):
    return format(int(a, 2) ^ int(b, 2), f'0{len(a)}b')


def keys(key):
    key = permute(key, P10)
    l, r = shift(key[:5], 1), shift(key[5:], 1)
    k1 = permute(l + r, P8)
    l, r = shift(l, 2), shift(r, 2)
    k2 = permute(l + r, P8)
    return k1, k2


def sbox(bits, box):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1:3], 2)
    return format(box[row][col], '02b')


def fk(bits, key):
    l, r = bits[:4], bits[4:]
    x = xor(permute(r, EP), key)
    y = permute(sbox(x[:4], S0) + sbox(x[4:], S1), P4)
    return xor(l, y) + r


def crypt(bits, k1, k2):
    bits = permute(bits, IP)
    bits = fk(bits, k1)
    bits = bits[4:] + bits[:4]
    bits = fk(bits, k2)
    return permute(bits, IP_INV)


key = input("Enter 10-bit key: ")
pt = input("Enter 8-bit plaintext: ")

if len(key) == 10 and len(pt) == 8 and set(key + pt) <= {'0', '1'}:
    k1, k2 = keys(key)

    ct = crypt(pt, k1, k2)
    decrypted = crypt(ct, k2, k1)

    print("K1         :", k1)
    print("K2         :", k2)
    print("Ciphertext :", ct)
    print("Decrypted  :", decrypted)
else:
    print("Enter a 10-bit key and an 8-bit plaintext.")
