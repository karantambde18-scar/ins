
# Caesar Cipher

def caesar_cipher(text, shift, mode):

    result = ""

    if mode == 'decrypt':
        shift = -shift

    for char in text:

        if 'a' <= char <= 'z':
            start = ord('a')
            new_position = (ord(char) - start + shift) % 26
            result += chr(start + new_position)

        elif 'A' <= char <= 'Z':
            start = ord('A')
            new_position = (ord(char) - start + shift) % 26
            result += chr(start + new_position)

        else:
            result += char

    return result


# Example Usage

message = "Hello, World!"
shift_amount = 3

# Encrypt
encrypted_text = caesar_cipher(message, shift_amount, 'encrypt')

print("Original:", message)
print("Encrypted:", encrypted_text)

# Decrypt
decrypted_text = caesar_cipher(encrypted_text, shift_amount, 'decrypt')

print("Decrypted:", decrypted_text)
