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

# Parameters for Henon-Heiles map
A = 1.0
B = 0.3
C = 0.2
D = 0.1
num_iterations = 512 * 512  # Total keystream length

# Initial conditions
x = [0.1]
y = [0.3]

# Generate keystream using Henon-Heiles equations
for i in range(num_iterations - 1):
    x_next = y[i]
    y_next = -A * x[i] - B * y[i] - C * x[i]**2 - D * x[i] * y[i]
    
    x.append(x_next)
    y.append(y_next)

# Convert keystream to NumPy array
keystream = np.array([x, y])

# Save the original keystream
# np.savetxt("henon_heiles_keystream512.txt", keystream, fmt='%.8f')

# Modify the first value by flipping 1-bit in x[0]
keystream[0, 0] = flip_lsb(keystream[0, 0])

# Save the modified keystream
np.savetxt("henon_heiles_keystream512_modified.txt", keystream, fmt='%.8f')

# Time taken
toc = time.time()
print('Henon-Heiles Keystream generated and saved as:')
print('  - Original: henon_heiles_keystream512.txt')
print('  - 1-bit changed: henon_heiles_keystream512_modified.txt')
print(f'Time taken for keystream generation: {toc - tic:.4f} seconds')
