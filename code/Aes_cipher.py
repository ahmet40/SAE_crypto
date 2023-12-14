from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import binascii


def generate_aes_key():
    """
        Generates a random 256-bit AES key.
    """
    return get_random_bytes(32)  # 32 bytes = 256 bits

def aes_encrypt(message, key):
    """
        Encrypts the given message using the given key.
    """
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return ciphertext, cipher.iv

def aes_decrypt(ciphertext, key, iv):
    """
        Decrypts the given ciphertext using the given key and iv.
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(ciphertext)
    decrypted_message = unpad(decrypted_bytes, AES.block_size)
    return decrypted_message.decode('utf-8',errors="replace")
