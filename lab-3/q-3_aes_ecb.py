from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
from skimage import io
import os
img = Image.open('D:\Cyber Security\lab-2\Lab3_image.jpg')
img_data = img.tobytes()

# Generate a secret key for AES encryption
key = os.urandom(16)

# ECB mode encryption
cipher_ecb = AES.new(key, AES.MODE_ECB)
encrypted_data_ecb = cipher_ecb.encrypt(pad(img_data, AES.block_size))
encrypted_img_ecb = Image.frombytes(img.mode, img.size, encrypted_data_ecb)
encrypted_img_ecb.save('encrypted_image_ecb.png')

# CBC mode encryption
iv = os.urandom(16)
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
encrypted_data_cbc = cipher_cbc.encrypt(pad(img_data, AES.block_size))
encrypted_img_cbc = Image.frombytes(img.mode, img.size, encrypted_data_cbc)
encrypted_img_cbc.save('encrypted_image_cbc.png')

# Compare the two encrypted image files
with open('encrypted_image_ecb.png', 'rb') as f1, open('encrypted_image_cbc.png', 'rb') as f2:
    if f1.read() == f2.read():
        print("The two encrypted image files are the same.")
    else:
        print("The two encrypted image files are different.")

# Decryption using ECB mode
cipher_ecb = AES.new(key, AES.MODE_ECB)
decrypted_data_ecb = unpad(cipher_ecb.decrypt(encrypted_data_ecb), AES.block_size)
decrypted_img_ecb = Image.frombytes(img.mode, img.size, decrypted_data_ecb)
decrypted_img_ecb.save('decrypted_image_ecb.png')

# Decryption using CBC mode
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
decrypted_data_cbc = unpad(cipher_cbc.decrypt(encrypted_data_cbc), AES.block_size)
decrypted_img_cbc = Image.frombytes(img.mode, img.size, decrypted_data_cbc)
decrypted_img_cbc.save('decrypted_image_cbc.png')

with open('decrypted_image_ecb.png', 'rb') as f1, open('decrypted_image_cbc.png', 'rb') as f2:
    if f1.read() == f2.read():
        print("The two decrypted image files are the same.")
    else:
        print("The two decrypted image files are different.")
