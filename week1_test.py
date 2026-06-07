from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

message = b"Cryptography Environment Setup Successful!"

cipher_text = cipher_suite.encrypt(message)
plain_text = cipher_suite.decrypt(cipher_text)

print("Original text:", message.decode())
print("Encrypted text:", cipher_text)
print("Decrypted text:", plain_text.decode())