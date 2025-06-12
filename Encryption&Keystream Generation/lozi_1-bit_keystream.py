import numpy as np
import time
import struct

# Function to flip the least significant bit (LSB) of a floating-point number
def flip_lsb(value):
    """Flip the least significant bit (LSB) of a floating-point number."""
    packed = struct.pack('d', value)  # Convert float to bytes (IEEE 754)
    unpacked = struct.unpack('Q', packed)[0]  # Convert bytes to integer
    flipped = unpacked ^ 1  # Flip the LSB
    return struct.unpack('d', struct.pack('Q', flipped))[0]  # Convert back to float

# Start timing
tic = time.time()

# Parameters for Lozi map
a = 1.4
b = 0.3
num_iterations = 1024 * 1024  # Total keystream length

# Initial conditions
x = [0.1]
y = [0.3]

# Generate keystream using Lozi map equations
for i in range(num_iterations - 1):
    x_next = 1 - a * abs(x[i]) + y[i]
    y_next = b * x[i]
    
    x.append(x_next)
    y.append(y_next)

# Convert to NumPy array
keystream = np.array([x, y])

# Save the original keystream
# np.savetxt('lozi_keystream1024.txt', keystream, fmt='%.8f')

# Modify the first value by flipping 1-bit in x[0]
keystream[0, 0] = flip_lsb(keystream[0, 0])

# Save the modified keystream
np.savetxt('lozi_keystream1024_modified.txt', keystream, fmt='%.8f')

# Time taken
toc = time.time()
print('Lozi Map Keystream generated and saved as:')
print('  - Original: lozi_keystream1024.txt')
print('  - 1-bit changed: lozi_keystream1024_modified.txt')
print(f'Time taken for keystream generation: {toc - tic:.4f} seconds')
