import hashlib

def calculate_sha1_digest(text):
    """
    Calculates the SHA-1 digest of the given text.
    :param text: The input text (string).
    :return: The SHA-1 hash digest in hexadecimal format.
    """
    # Encode the text to bytes
    text_bytes = text.encode('utf-8')

    # Create a SHA-1 hash object
    sha1 = hashlib.sha1()

    # Update the hash object with the text bytes
    sha1.update(text_bytes)

    # Get the hexadecimal digest
    digest = sha1.hexdigest()

    return digest

# Example usage
input_text = "Hello, World!"
sha1_digest = calculate_sha1_digest(input_text)

print(f"Input Text: {input_text}")
print(f"SHA-1 Digest: {sha1_digest}")
