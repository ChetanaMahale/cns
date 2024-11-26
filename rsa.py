# Simple RSA Implementation

from math import gcd

# Key generation
def generate_keys():
    p, q = 61, 53  # Two prime numbers
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 3
    while gcd(e, phi) != 1:
        e += 2  # Increment by 2 to ensure e remains odd (odd numbers are more likely to be coprime)
    
    # Calculate modular inverse of e
    d = pow(e, -1, phi)
    
    return (e, n), (d, n)  # Public and Private keys

# Encryption
def encrypt(public_key, plaintext):
    e, n = public_key
    return [(ord(char) ** e) % n for char in plaintext]

# Decryption
def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr((char ** d) % n) for char in ciphertext])

# Example usage
public_key, private_key = generate_keys()
message = "HELLO"
encrypted = encrypt(public_key, message)
decrypted = decrypt(private_key, encrypted)

print("Public Key:", public_key)
print("Private Key:", private_key)
print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
