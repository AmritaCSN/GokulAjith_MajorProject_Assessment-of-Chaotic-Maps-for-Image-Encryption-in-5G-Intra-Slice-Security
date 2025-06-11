import numpy as np  # Import numpy at the top of your script
import time

# Start timing
tic = time.time()

# Parameters
K = 0.8  # Chirikov map parameter
num_iterations = 1024 * 1024 # Total number of iterations

# Initial conditions
x = [0.8]
y = [0.9]

# Generating the X and Y sequences using the Chirikov map
for i in range(num_iterations - 1):
    x_next = x[i] + K * np.sin(y[i])
    y_next = y[i] + x_next
    
    x.append(x_next % (2 * np.pi))  # Keep values within a bounded range
    y.append(y_next % (2 * np.pi))

# Convert to NumPy array
keystream = np.array([x, y])

# Save to a text file
np.savetxt("C:/Users/GOKUL AJITH/major/Keystream/chirikov_keystream1024.txt", keystream, fmt='%.8f')

print('Chirikov Map Keystream generated and saved as chirikov_keystream1024.txt.')

# Time taken
toc = time.time()
print(f'Time taken for keystream generation: {toc - tic:.4f} seconds')
