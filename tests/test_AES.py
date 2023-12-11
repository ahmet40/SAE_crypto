import unittest
import sys
import os

ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')
sys.path.append(os.path.join(ROOT,'code/'))
from Aes import generate_aes_key, aes_decrypt, aes_encrypt

class TestAES(unittest.TestCase):

    def test_AES(self):
        key = generate_aes_key()
        message = "Hello, world!"
        encrypted_text, iv = aes_encrypt(message, key)
        self.assertTrue(encrypted_text)
        decrypted_text = aes_decrypt(encrypted_text, key, iv)
        self.assertEqual(decrypted_text, message)


if __name__ == '__main__':
    unittest.main()
