# ECC Key Generation and Encryption/Decryption (basic)

p = 17
a = 2
b = 2
G = (5, 1)

# Point addition
def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 != y2:
        return None

    if P == Q:
        m = (3*x1*x1 + a) * pow(2*y1, -1, p) % p
    else:
        m = (y2-y1) * pow(x2-x1, -1, p) % p

    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1-x3) - y1) % p

    return (x3, y3)

# Point multiplication
def multiply(k, P):
    R = None
    while k:
        if k & 1:
            R = add(R, P)
        P = add(P, P)
        k >>= 1
    return R

# Key generation
private_key = 5
public_key = multiply(private_key, G)

print("Private Key:", private_key)
print("Public Key:", public_key)

# Encryption key (shared secret)
other_private = 7
other_public = multiply(other_private, G)

shared1 = multiply(private_key, other_public)
shared2 = multiply(other_private, public_key)

print("Shared Secret 1:", shared1)
print("Shared Secret 2:", shared2)
