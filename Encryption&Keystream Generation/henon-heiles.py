import numpy as np
import time

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

# Convert to NumPy array
keystream = np.array([x, y])
print(keystream.shape)
# Save keystream to a file
np.savetxt('C:/Users/GOKUL AJITH/major/Keystream/henon_heiles_keystream128.txt', keystream, fmt='%.8f')

print('Henon-Heiles Keystream generated and saved as henon_heiles_keystream.txt.')

# Time taken
toc = time.time()
print(f'Time taken for keystream generation: {toc - tic:.4f} seconds')
