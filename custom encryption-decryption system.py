#Step 1: Create a Substitution Cipher Algorithm
def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) + key - shift) % 26 + shift)
        else:
            encrypted_message += char
    return encrypted_message

# Example usage:
message = "Hello, World!"
key = 3
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)
#Decryption
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - key - shift) % 26 + shift)
        else:
            decrypted_message += char
    return decrypted_message

# Example usage:
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
#Step 3: Optional Multi-Layer Encryption
def multi_layer_encrypt(message, keys):
    for key in keys:
        message = encrypt(message, key)
    return message

def multi_layer_decrypt(encrypted_message, keys):
    for key in reversed(keys):
        encrypted_message = decrypt(encrypted_message, key)
    return encrypted_message

# Example usage:
keys = [3, 5]  # Multiple keys for multi-layer encryption
multi_layer_encrypted_message = multi_layer_encrypt(message, keys)
print("Multi-layer Encrypted message:", multi_layer_encrypted_message)
multi_layer_decrypted_message = multi_layer_decrypt(multi_layer_encrypted_message, keys)
print("Multi-layer Decrypted message:", multi_layer_decrypted_message)
