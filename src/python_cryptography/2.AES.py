# Key must be of fixe sized - 128 bit example Use MD5

# IV  - Initialization Vector - must be RANDOM

# Block SIZE - 128 bits (PAD & UNPAD)

# from hashlib import AES
from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
import base64


class AESCrypto:

    def md5_hash(self, text):
        h = MD5.new()
        h.update(text.encode('utf-8'))
        return h.hexdigest()

    def __init__(self, key):
        self.key = self.md5_hash(key)

    def enctrypt(self, cleartext):
        # Block size should be equal to 128 bits
        Block_size = 16

        def pad(s): return s + (Block_size - len(s) %
                                Block_size) * chr(Block_size - len(s)
                                                  % Block_size)
        cleartext_blocks = pad(cleartext)

        # create random IV
        iv = Random.new().read(Block_size)
        crypto = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + crypto.encrypt(cleartext_blocks))

    def decrypt(self, enctext):
        enctext = base64.b64encode(enctext)
        iv = enctext[:16]
        crypto = AES.new(self.key, AES.MODE_CBC, iv)

        # unpad the blocks before decrypting
        def unpad(s): return s[0:-ord(s[-1])]
        return unpad(crypto.decrypt(enctext[16:]))


aes = AESCrypto('Password123')
encrypted = aes.enctrypt("Hellow world")
print(encrypted)

decrpted = aes.decrypt(encrypted)
print(decrpted)
