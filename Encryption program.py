import random as r
import string as s

chars = " " + s.digits + s.ascii_letters + s.punctuation
chars =list(chars)
key = chars.copy()

r.shuffle(key)

print(f'chars: {chars}')
print(f'key: {key}')

#ENCRYPTION

plain_text = input('Enter a message to encrypt : ')
cyber_text = ""


for letter in plain_text:
    index = chars.index(letter)
    cyber_text += key[index]


print(f'Original Message: {plain_text}')
print(f'Encrypted Message: {cyber_text}')


#DECRYPTION
cyber_text = input('Enter a message to decrypt : ')
plain_text= ""


for letter in cyber_text:
    index = key.index(letter)
    plain_text += chars[index]


print(f'Encrypted Message: {cyber_text}')
print(f'Original Message: {plain_text}')