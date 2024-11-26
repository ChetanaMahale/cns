# Simulating Diffie-Hellman with MITM attack

import random

# Function to simulate power modulo (a^b % p)
def power_mod(base, exp, mod):
    return pow(base, exp, mod)

# Diffie-Hellman participants
class Participant:
    def __init__(self, name, p, g):
        self.name = name
        self.p = p
        self.g = g
        self.private_key = random.randint(2, p - 2)  # Choose private key
        self.public_key = power_mod(g, self.private_key, p)  # Compute public key
    
    def compute_shared_secret(self, other_public_key):
        return power_mod(other_public_key, self.private_key, self.p)

# Man-in-the-Middle Attacker
class Attacker:
    def __init__(self, p, g):
        self.p = p
        self.g = g
        self.private_key = random.randint(2, p - 2)
        self.public_key = power_mod(g, self.private_key, p)
    
    def intercept_and_replace(self, original_key):
        # Intercept and return attacker's public key instead of the original
        return self.public_key

    def compute_shared_secret(self, other_public_key):
        return power_mod(other_public_key, self.private_key, self.p)

# Example of Diffie-Hellman with MITM attack
def main():
    # Prime number (p) and generator (g)
    p = 23  # Small prime number for simplicity
    g = 5   # Generator
    
    # Participants
    alice = Participant("Alice", p, g)
    bob = Participant("Bob", p, g)
    mallory = Attacker(p, g)  # Man-in-the-middle
    
    # Step 1: Alice sends her public key to Bob
    alice_public_key = alice.public_key
    intercepted_by_mallory = mallory.intercept_and_replace(alice_public_key)
    
    # Step 2: Mallory sends her fake public key to Bob
    bob_received_key = intercepted_by_mallory
    
    # Step 3: Bob sends his public key to Alice
    bob_public_key = bob.public_key
    intercepted_by_mallory_bob = mallory.intercept_and_replace(bob_public_key)
    
    # Step 4: Mallory sends her fake public key to Alice
    alice_received_key = intercepted_by_mallory_bob
    
    # Alice computes her "shared secret"
    alice_shared_secret = alice.compute_shared_secret(alice_received_key)
    
    # Bob computes his "shared secret"
    bob_shared_secret = bob.compute_shared_secret(bob_received_key)
    
    # Mallory computes secrets with Alice and Bob
    mallory_shared_with_alice = mallory.compute_shared_secret(alice_public_key)
    mallory_shared_with_bob = mallory.compute_shared_secret(bob_public_key)
    
    # Outputs
    print("=== Keys ===")
    print(f"Alice's Public Key: {alice_public_key}")
    print(f"Bob's Public Key: {bob_public_key}")
    print(f"Mallory's Fake Public Key: {mallory.public_key}")
    
    print("\n=== Shared Secrets ===")
    print(f"Alice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")
    print(f"Mallory's Shared Secret with Alice: {mallory_shared_with_alice}")
    print(f"Mallory's Shared Secret with Bob: {mallory_shared_with_bob}")
    
    print("\n=== Results ===")
    if alice_shared_secret == bob_shared_secret:
        print("Secure Communication: Shared secrets match.")
    else:
        print("Insecure Communication: Man-in-the-middle attack succeeded!")
        print(f"Mallory can decrypt and re-encrypt messages.")

# Run the simulation
main()
