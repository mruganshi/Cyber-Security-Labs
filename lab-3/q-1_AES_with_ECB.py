from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
key = b'B20CS014GOHEL000'
cipher = AES.new(key, AES.MODE_ECB)
plaintext = b'This is a secret message'
print("Original message: ",plaintext)
padded_plaintext = pad(plaintext, AES.block_size)
ciphertext = cipher.encrypt(padded_plaintext)
print("Ciphertext: ",ciphertext)
cipher = AES.new(key, AES.MODE_ECB)
decrypted_plaintext = cipher.decrypt(ciphertext)
unpadded_plaintext = unpad(decrypted_plaintext, AES.block_size)
print("Decrypted message: ",unpadded_plaintext) 
