
# Vigenere Cipher - Encryption

def vigenere_cipher(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    plaintext = plaintext.upper()
    ciphertext = ''
    key_index = 0

    for char in plaintext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            char_index = alphabet.index(char)
            new_index = (char_index + shift) % 26

            ciphertext += alphabet[new_index]
            key_index += 1
        else:
            ciphertext += char

    return ciphertext


# Vigenere Cipher - Decryption

def vigenere_decipher(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    ciphertext = ciphertext.upper()
    plaintext = ''
    key_index = 0

    for char in ciphertext:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            char_index = alphabet.index(char)
            new_index = (char_index - shift + 26) % 26

            plaintext += alphabet[new_index]
            key_index += 1
        else:
            plaintext += char

    return plaintext


# Test Example

plaintext = "INFORMATION"
key = "KEY"

ciphertext = vigenere_cipher(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = vigenere_decipher(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
