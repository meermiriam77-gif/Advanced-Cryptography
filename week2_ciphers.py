def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text.upper():
        if char.isalpha():
            shift_val = shift if encrypt else -shift
            result += chr((ord(char) - 65 + shift_val) % 26 + 65)
        else:
            result += char
    return result

def vigenere_cipher(text, key, encrypt=True):
    result, key_idx = "", 0
    key = key.upper()
    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - 65
            shift = shift if encrypt else -shift
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_idx += 1
        else:
            result += char
    return result

print("--- Classical Cipher Testing ---")
user_input = input("Enter text to encrypt (letters only): ")

# Input Validation Check
if not user_input.replace(" ", "").isalpha():
    print("Error: Invalid input! Please use alphabet characters only.")
else:
    print("\n[Caesar Cipher - Shift 4]")
    c_enc = caesar_cipher(user_input, 4)
    print(f"Encrypted: {c_enc}")
    print(f"Decrypted: {caesar_cipher(c_enc, 4, False)}")

    print("\n[Vigenère Cipher - Key: CRYPTO]")
    v_enc = vigenere_cipher(user_input, "CRYPTO")
    print(f"Encrypted: {v_enc}")
    print(f"Decrypted: {vigenere_cipher(v_enc, 'CRYPTO', False)}")