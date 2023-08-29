from Crypto.Cipher import DES3
import base64
plaintext = b'This is a secret message'
key = b'B20CS014GOHEL000'
iv = b'ThisisIV'
print('Original plaintext:', plaintext)
cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext: ",ciphertext)
cipher2 = DES3.new(key, DES3.MODE_CBC, iv=iv)
decrypted_padded_plaintext = cipher2.decrypt(ciphertext)
print('Decrypted plaintext:', decrypted_padded_plaintext)
