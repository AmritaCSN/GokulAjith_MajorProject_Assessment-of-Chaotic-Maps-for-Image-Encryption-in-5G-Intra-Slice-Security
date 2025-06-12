import numpy as np
import time
import struct

# Start timing
tic = time.time()

# Parameters
K = 0.8  # Chirikov map parameter
num_iterations = 128 * 128  # Total number of iterations

# **Function to flip the least significant bit (LSB) of a floating-point number**
def flip_lsb(value):
    """Flip the least significant bit of a floating-point value."""
    packed = struct.pack('d', value)  # Convert float to bytes (IEEE 754)
    unpacked = struct.unpack('Q', packed)[0]  # Convert bytes to integer
    flipped = unpacked ^ 1  # Flip the least significant bit (LSB)
    return struct.unpack('d', struct.pack('Q', flipped))[0]  # Convert back to float

# **Original Keystream Generation**
x_orig = [0.8]
y_orig = [0.9]

for i in range(num_iterations - 1):
    x_next = x_orig[i] + K * np.sin(y_orig[i])
    y_next = y_orig[i] + x_next

    x_orig.append(x_next % (2 * np.pi))
    y_orig.append(y_next % (2 * np.pi))

keystream_orig = np.array([x_orig, y_orig])
# np.savetxt("C:/Users/GOKUL AJITH/major/chirikov_keystream128.txt", keystream_orig, fmt='%.8f')

# **Modified Keystream Generation (1-bit changed)**
x_mod = [flip_lsb(0.8)]  # Modify only the initial x value
y_mod = [0.9]

for i in range(num_iterations - 1):
    x_next = x_mod[i] + K * np.sin(y_mod[i])
    y_next = y_mod[i] + x_next

    x_mod.append(x_next % (2 * np.pi))
    y_mod.append(y_next % (2 * np.pi))

keystream_mod = np.array([x_mod, y_mod])
np.savetxt("C:/Users/GOKUL AJITH/major/chirikov_keystream128_modified.txt", keystream_mod, fmt='%.8f')

print('Chirikov Map Keystream generated and saved as:')
print('  - Original: chirikov_keystream128.txt')
print('  - 1-bit changed: chirikov_keystream128_modified.txt')

# Time taken
toc = time.time()
print(f'Time taken for keystream generation: {toc - tic:.4f} seconds')
