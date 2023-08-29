from Crypto.Cipher import DES3
plaintext = b'This is a secret message'
key = b'B20CS014GOHEL000'
iv = b'Thisisan'
print('Original plaintext:', plaintext)
cipher = DES3.new(key, DES3.MODE_OFB, iv=iv)
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext: ",ciphertext)
cipher2 = DES3.new(key, DES3.MODE_OFB, iv=iv)
decrypted_padded_plaintext = cipher2.decrypt(ciphertext)
print('Decrypted plaintext:', decrypted_padded_plaintext)
