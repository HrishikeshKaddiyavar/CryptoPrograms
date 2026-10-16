# ElGamal Encryption and Decryption

# Public parameters
p = 23
g = 5

# Key Generation
x = 6                  # Private key
y = pow(g, x, p)       # Public key

print("Public key:", (p, g, y))
print("Private key:", x)

# Message
M = 10

# Random encryption key (fixed for demonstration)
k = 3

# Encryption
C1 = pow(g, k, p)
C2 = (M * pow(y, k, p)) % p

print("Original message:", M)
print("Encrypted message:", (C1, C2))

# Decryption
S = pow(C1, x, p)
S_inv = pow(S, -1, p)

decrypted = (C2 * S_inv) % p

print("Decrypted message:", decrypted)
