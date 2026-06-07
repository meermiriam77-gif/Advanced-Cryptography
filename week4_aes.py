import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

aes_key = os.urandom(32) 
iv = os.urandom(16)      

print("=== AES Key Generation ===")
print(f"Generated AES-256 Key (Hex): {aes_key.hex()}")

file_content = b"This is a highly confidential document for Advanced Cryptography."
print(f"\nOriginal File Content: {file_content.decode()}")

start_time = time.perf_counter()

padder = padding.PKCS7(128).padder()
padded_data = padder.update(file_content) + padder.finalize()

cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
encryptor = cipher.encryptor()
encrypted_file = encryptor.update(padded_data) + encryptor.finalize()

enc_time = time.perf_counter()

print(f"\n=== File Encryption Demonstration ===")
print(f"Encrypted Data (Hex): {encrypted_file.hex()}")

decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(encrypted_file) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
decrypted_file = unpadder.update(decrypted_padded) + unpadder.finalize()

dec_time = time.perf_counter()

print(f"\n=== Decryption Results ===")
print(f"Decrypted Content: {decrypted_file.decode()}")

print(f"\n=== AES Performance Testing ===")
print(f"Encryption Time: {(enc_time - start_time) * 1000:.4f} milliseconds")
print(f"Decryption Time: {(dec_time - enc_time) * 1000:.4f} milliseconds")