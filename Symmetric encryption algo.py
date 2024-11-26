import random

def feistel_encrypt_decrypt(block, keys, num_rounds, decrypt=False):
    """
    Perform Feistel encryption or decryption on a block.
    :param block: Input block to encrypt or decrypt (as bytes or integers).
    :param keys: List of round keys.
    :param num_rounds: Number of rounds in the Feistel structure.
    :param decrypt: Boolean flag to indicate decryption.
    :return: Encrypted or decrypted block.
    """
    # Split block into two halves
    left, right = block[:len(block)//2], block[len(block)//2:]
    
    # Reverse keys for decryption
    if decrypt:
        keys = keys[::-1]

    for round_key in keys:
        new_left = right
        # Apply the Feistel function (XOR for simplicity)
        right = bytes([l ^ feistel_function(r, round_key) for l, r in zip(left, right)])
        left = new_left

    return left + right

def feistel_function(block_part, key):
    """
    A simple Feistel function for the block.
    :param block_part: A single byte (integer).
    :param key: Current round key.
    :return: Transformed byte (integer).
    """
    return (block_part + key) % 256



def generate_keys(num_rounds, seed=None):
    """
    Generate round keys for the Feistel structure.
    :param num_rounds: Number of rounds.
    :param seed: Optional seed for reproducibility.
    :return: List of keys.
    """
    if seed:
        random.seed(seed)
    return [random.randint(0, 255) for _ in range(num_rounds)]


def pad_block(data, block_size):
    """
    Pads the input to make it a multiple of the block size.
    """
    padding_length = block_size - (len(data) % block_size)
    return data + bytes([padding_length] * padding_length)


def unpad_block(data):
    """
    Removes padding from the input.
    """
    padding_length = data[-1]
    return data[:-padding_length]


# Parameters
block_size = 8  # 64-bit block size
num_rounds = 8  # Number of Feistel rounds
seed = 42       # Seed for reproducible key generation

# Example usage
keys = generate_keys(num_rounds, seed=seed)

# Input data (must be padded to the block size)
data = b"Hello World!"
padded_data = pad_block(data, block_size)

# Encrypt the data block by block
encrypted_blocks = []
for i in range(0, len(padded_data), block_size):
    block = padded_data[i:i+block_size]
    encrypted_blocks.append(feistel_encrypt_decrypt(block, keys, num_rounds))

encrypted_data = b"".join(encrypted_blocks)

# Decrypt the data block by block
decrypted_blocks = []
for i in range(0, len(encrypted_data), block_size):
    block = encrypted_data[i:i+block_size]
    decrypted_blocks.append(feistel_encrypt_decrypt(block, keys, num_rounds, decrypt=True))

decrypted_data = unpad_block(b"".join(decrypted_blocks))

# Display results
print(f"Original Data: {data}")
print(f"Encrypted Data: {encrypted_data}")
print(f"Decrypted Data: {decrypted_data}")
