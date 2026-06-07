import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

print("=== 1. RSA Key Pair Generation ===")
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()
print("RSA 2048-bit Private Key Generated.")
print("RSA 2048-bit Public Key Extracted.")

print("\n=== 2. Public Key Encryption Process ===")
message = b"Confidential transmission: Final phase of advanced cryptography project."
print(f"Original Message: {message.decode()}")

start_time = time.perf_counter()

ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"Encrypted Ciphertext (Hex snippet): {ciphertext.hex()[:60]}...")

print("\n=== 3. Private Key Decryption Results ===")
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"Decrypted Message: {plaintext.decode()}")

print("\n=== 4. Secure Message Transmission & 5. Validation ===")
end_time = time.perf_counter()

if message == plaintext:
    print("Validation: SUCCESS - The decrypted message perfectly matches the original.")
else:
    print("Validation: FAILED - Data corruption detected.")
    
print(f"Total RSA workflow executed in {(end_time - start_time) * 1000:.4f} milliseconds.")