import hashlib

# Generate keys
p = 23
q = 11
g = 4
x = 3                  # Private key
y = pow(g, x, p)       # Public key

# Message
message = "Hello World"

# Generate signature
k = 7
h = int(hashlib.sha256(message.encode()).hexdigest(), 16)

r = pow(g, k, p) % q
s = (pow(k, -1, q) * (h + x * r)) % q

print("Signature:", r, s)

# Verify signature
w = pow(s, -1, q)
u1 = (h * w) % q
u2 = (r * w) % q

v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

if v == r:
    print("Signature Verified")
else:
    print("Invalid Signature")
