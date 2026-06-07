import time

def lfsr(seed, taps, length):
    state = seed[:]
    out = []
    for _ in range(length):
        out.append(state[-1])
        xor_res = sum([state[i] for i in taps]) % 2
        state = [xor_res] + state[:-1]
    return out

def frequency_test(sequence):
    zeros = sequence.count(0)
    ones = sequence.count(1)
    print(f"Frequency Test -> 0s: {zeros}, 1s: {ones}")
    
    if abs(zeros - ones) <= len(sequence) * 0.2:
        print("Result: Good Randomness (Balanced)")
    else:
        print("Result: Poor Randomness (Unbalanced)")

def rc4_encrypt(text, key_string):
    key = [ord(c) for c in key_string]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    i = j = 0
    encrypted = []
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream_byte = S[(S[i] + S[j]) % 256]
        encrypted.append(ord(char) ^ keystream_byte)
    return encrypted

print("=== LFSR Generation & Randomness Testing ===")
seed_val = [1, 0, 1, 1, 0]
tap_positions = [0, 2] 
seq = lfsr(seed_val, tap_positions, 50)

print(f"LFSR Output (50 bits): {seq}")
frequency_test(seq)

print("\n=== RC4 Stream Cipher ===")
message = "AdvancedCryptography"
secret_key = "securekey"

start_time = time.perf_counter()
encrypted_msg = rc4_encrypt(message, secret_key)
end_time = time.perf_counter()

print(f"Original Text: {message}")
print(f"RC4 Encrypted (Hex): {[hex(c) for c in encrypted_msg]}")
print(f"Performance: Encrypted in {(end_time - start_time) * 1000:.4f} milliseconds")