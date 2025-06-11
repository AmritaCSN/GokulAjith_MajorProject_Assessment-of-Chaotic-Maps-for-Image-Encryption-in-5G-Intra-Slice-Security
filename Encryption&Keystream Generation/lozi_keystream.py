import numpy as np
import time

# Start timing
tic = time.time()

# Parameters for Lozi map
a = 1.4
b = 0.3
num_iterations = 1024 * 1024 # Total keystream length

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

# Save keystream to a file
np.savetxt('C:/Users/GOKUL AJITH/major/Keystream/lozi_keystream1024.txt', keystream, fmt='%.8f')


print('Lozi Map Keystream generated and saved as lozi_keystream.txt.')

# Time taken
toc = time.time()
print(f'Time taken for keystream generation: {toc - tic:.4f} seconds')
