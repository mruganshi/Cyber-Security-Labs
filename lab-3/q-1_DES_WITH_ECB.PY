from Crypto.Cipher import DES3
import base64
plaintext = b'This is a secret message'
key = b'B20CS014GOHEL000'
print('Original plaintext:', plaintext)
cipher = DES3.new(key, DES3.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)
print('ciphertext:', ciphertext)
decrypted_padded_plaintext = cipher.decrypt(ciphertext)
print('Decrypted plaintext:', decrypted_padded_plaintext)
