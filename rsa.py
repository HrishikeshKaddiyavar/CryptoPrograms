# RSA Rivest–Shamir–Adleman Algorithm

import math

# 2 prime nums
p = int(input("Enter value of p: "))
q = int(input("Enter value of q: "))

# calc n
n = p*q

# calc Euler's totient fun
phi = (p-1)*(q-1)

e = int(input("Enter value of e: "))

if not ((1 < e < phi) and (math.gcd(e,phi) == 1)):
	print("Invalid e value!")
else:
	d = 1
	
	while ((d*e)%phi) != 1:
		d += 1
	
	print("Public key: ", (e,n))
	print("Private key: ", (d,n))
	
	m = int(input("Enter plaintext: "))
	
	# encryption
	c = pow(m,e,n)
	print("Cipher text: ",c)
	
	# decryption
	decrypted = pow(c,d,n)
	print("Decrypted text: ",decrypted)

	

