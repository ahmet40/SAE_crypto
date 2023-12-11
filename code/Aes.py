from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_aes_key():
    return get_random_bytes(32)  # 32 bytes = 256 bits

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return ciphertext, cipher.iv

def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode('utf-8')

# Exemple d'utilisation
key = generate_aes_key()
message = "Hello, world!"
encrypted_text, iv = aes_encrypt(message, key)
decrypted_text = aes_decrypt(encrypted_text, key, iv)

print(f"Message d'origine: {message}")
print(f"Texte chiffré: {encrypted_text}")
print(f"Texte déchiffré: {decrypted_text}")
