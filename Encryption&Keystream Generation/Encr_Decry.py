#importing required libraries
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
import os
from PIL import Image
import time
import psutil

# Get memory usage for the current process
process = psutil.Process(os.getpid())

#memory and time start
start_memory = process.memory_info().rss
start_time = time.time()

# Reading the encryption key
with open(r"C:/USERS/GOKUL AJITH/major/Keystream/henon_heiles_keystream1024.txt", 'rb') as key_file:      
    keystream = [int(float(num)) for line in key_file for num in line.split()]
key_bytes = bytes(keystream[:32])
# IV generation
iv = os.urandom(16)
# Opening image 
image_path = r"C:/USERS/GOKUL AJITH/image_dataset/1024 x 1024.png"
plain_image = Image.open(image_path)
image_bytes = plain_image.tobytes()
#cipher object created
chacha20_cipher = Cipher(algorithms.ChaCha20(key_bytes, iv),mode=None)
#encryption
chacha20_encryptor = chacha20_cipher.encryptor()
encrypted_image_bytes = chacha20_encryptor.update(image_bytes) + chacha20_encryptor.finalize()
encrypted_image = Image.frombytes('RGB', plain_image.size, encrypted_image_bytes)
encrypted_image_path = r"C:/USERS/GOKUL AJITH/major/Encrypted/1024_HHM_encrypted.png"
encrypted_image.save(encrypted_image_path)
print("Encrypted Image Saved at:", encrypted_image_path)
#decryption
chacha20_decryptor = chacha20_cipher.decryptor()
decrypted_image_bytes = chacha20_decryptor.update(encrypted_image_bytes) + chacha20_decryptor.finalize()
decrypted_image = Image.frombytes('RGB', encrypted_image.size, decrypted_image_bytes)
decrypted_image_path = r"C:/USERS/GOKUL AJITH/major/Decrypted/1024_HHM_decrypted.png" #1024 1-bit changed plain image  cm decrypted changed
decrypted_image.save(decrypted_image_path)
print("Decrypted Image Saved at:", decrypted_image_path)

#time and memory end
elapsed_time = time.time() - start_time
end_memory = process.memory_info().rss
memory_used = (end_memory - start_memory) / (1024 * 1024)  # in MB

print("end-to-end time taken:", elapsed_time, "seconds")
print("end-to-end memory usage:", memory_used, "MB")
