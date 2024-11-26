# Initial Permutation (IP) Table
IP = [1, 5, 2, 0, 3, 7, 4, 6]

# Inverse Permutation (IP-1) Table
IP_INV = [3, 0, 2, 4, 6, 1, 7, 5]

# Expansion Table for right half
E = [3, 0, 1, 2, 1, 2, 3, 0]

# Permutation P Table
P = [1, 3, 2, 0]

# S-Boxes
SBOX1 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

SBOX2 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

# Helper: Permutation Function
def permute(bits, table):
    return [bits[i] for i in table]

# Helper: XOR Function
def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

# Helper: Split Bits
def split_bits(bits):
    mid = len(bits) // 2
    return bits[:mid], bits[mid:]

# Helper: S-Box Substitution
def sbox_substitution(bits):
    left, right = split_bits(bits)
    
    # Convert to row and column indices for S-Box
    row1 = (left[0] << 1) + left[3]
    col1 = (left[1] << 1) + left[2]
    row2 = (right[0] << 1) + right[3]
    col2 = (right[1] << 1) + right[2]
    
    # Apply S-Boxes
    sbox1_value = SBOX1[row1][col1]
    sbox2_value = SBOX2[row2][col2]
    
    # Convert to 4-bit output
    return [
        (sbox1_value >> 1) & 1, sbox1_value & 1,
        (sbox2_value >> 1) & 1, sbox2_value & 1
    ]

# Round Function
def feistel(right, key):
    # Expansion
    expanded = permute(right, E)
    # XOR with key
    xored = xor(expanded, key)
    # S-Box substitution
    substituted = sbox_substitution(xored)
    # Permutation
    return permute(substituted, P)

# Simple DES Encrypt Function
def des_encrypt(plaintext, key):
    # Apply initial permutation
    plaintext = permute(plaintext, IP)
    left, right = split_bits(plaintext)
    
    # Perform 2 rounds (for simplicity)
    for _ in range(2):
        temp = right
        right = xor(left, feistel(right, key))
        left = temp
    
    # Combine left and right
    combined = right + left  # Swap left and right
    # Apply inverse permutation
    return permute(combined, IP_INV)

# Simple DES Decrypt Function
def des_decrypt(ciphertext, key):
    # Apply initial permutation
    ciphertext = permute(ciphertext, IP)
    left, right = split_bits(ciphertext)
    
    # Perform 2 rounds in reverse
    for _ in range(2):
        temp = left
        left = xor(right, feistel(left, key))
        right = temp
    
    # Combine left and right
    combined = right + left  # Swap left and right
    # Apply inverse permutation
    return permute(combined, IP_INV)

# Example Usage
# Input plaintext and key as 8-bit binary arrays
plaintext = [1, 0, 1, 0, 1, 1, 0, 1]  # Example plaintext (binary)
key = [1, 0, 1, 0, 0, 1, 1, 1]       # Example key (binary)

print("Original Plaintext:", plaintext)

# Encrypt
encrypted = des_encrypt(plaintext, key)
print("Encrypted:", encrypted)

# Decrypt
decrypted = des_decrypt(encrypted, key)
print("Decrypted:", decrypted)
