# Diffie Hellman algorithm

# choose 2 inputs p:prime number and g:generator
p = int(input("Enter prime num p:"))
g = int(input("Enter generator num g:"))

# 2 parties Alice a and Bob b choose private key
a = int(input("Enter private key for a:"))
b = int(input("Enter private key for b:"))

# calculate public keys
A = (g**a)%p
B = (g**b)%p

# share, calculate share secret key
aK = (B**a)%p
bK = (A**b)%p

if aK == bK:
	print("Key exchange successful!")
else:
	print("Key exchange failed!")

