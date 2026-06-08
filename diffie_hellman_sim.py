import time

print("=== Secure Communications: Diffie-Hellman Key Exchange ===")
time.sleep(1)

# Publicly known variables (Usually very large numbers in real life)
p = 23 # Prime number
g = 5  # Primitive root modulo

print(f"[Network] Public variables established: Prime (p) = {p}, Base (g) = {g}\n")
time.sleep(1)

# Alice's Side
print("[Alice] Generating private key...")
a = 4 # Alice's secret private key
A = (g**a) % p
print(f"[Alice] Sending public value to Bob: {A}\n")
time.sleep(1)

# Bob's Side
print("[Bob] Generating private key...")
b = 3 # Bob's secret private key
B = (g**b) % p
print(f"[Bob] Sending public value to Alice: {B}\n")
time.sleep(1)

# The Hacking Attempt
print("[!] Intercepting traffic... Attacker sees A and B, but cannot derive the secret!\n")
time.sleep(1)

# The Magic (Shared Secret Derivation)
print("[Alice] Computing shared symmetric key...")
alice_secret = (B**a) % p

print("[Bob] Computing shared symmetric key...")
bob_secret = (A**b) % p

time.sleep(1)
print(f"=== Key Exchange Complete ===")
print(f"Alice's Derived Secret: {alice_secret}")
print(f"Bob's Derived Secret:   {bob_secret}")

if alice_secret == bob_secret:
    print("\n[SUCCESS] Both parties established an identical secret key without transmitting it!")