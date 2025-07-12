# Subtitle Cipher Encryption Program

import random
import string
from operator import index

chars = " " + string.punctuation + string.digits + string.ascii_letters # + string.whitespace
chars = list(chars)
key = chars.copy()

random.shuffle(key)
#print(f"Chars: {chars}")
#print(f"Key: {key}")

# ENCRYPT
plane_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plane_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plane_text}")
print(f"encrypted message: {cipher_text}")

# DECRYPT


ciphers_text = input("Enter a message to decrypt: ")
plane_text = ""

for letter in ciphers_text:
    index = key.index(letter)
    plane_text += chars[index]
print(f"decrypted message: {plane_text}")
