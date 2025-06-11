# GokulAjith_MajorProject_Assessment-of-Chaotic-Maps-for-Image-Encryption-in-5G-Intra-Slice-Security
This respository contains the code which does the the Key generation , Encryption and Decryption followed by the Security and Perfomance Analysis.The repo also cotains the block diagram and description of the project.

# OVERVIEW

With the rise of 5G, securing intra-slice communication is crucial due to the transmission of sensitive user data in resource-constrained environments. Traditional encryption methods struggle to balance security and efficiency, making chaos-based encryption a viable alternative. This study proposes a lightweight chaos-based encryption scheme combining Chirikov, Lozi, and Hénon-Heiles maps with ChaCha20 to secure 5G intra-slice communication. It achieves strong security, low computational cost, and real-time efficiency, outperforming traditional chaotic methods like 2D-LSCM, Baker’s map, and Arnold’s cat map, making it ideal for resource-constrained IoT environments.

# DATASETS

The dataset used for the image encryption experiments is sourced from Kaggle and comprises a combined collection from the well-known Set5 and Set14 datasets. The Set5 dataset, originally introduced in the paper "Low-Complexity Single Image Super-Resolution based on Nonnegative Neighbor Embedding" by Marco Bevilacqua et al., includes five commonly referenced images titled "baby," "bird," "butterfly," "head," and "woman." These images are widely used as standard benchmarks for evaluating the performance of single-image super-resolution models.For the purposes of this study, all images were used in color (.png format) and resized to four different resolutions: 128 × 128, 256 × 256, 512 × 512, and 1024 × 1024 pixels. This range of image sizes allows for a comprehensive evaluation of the proposed encryption scheme's scalability, consistency, and performance across varying levels of data complexity. 

# SOFTWARES/LIBRARIES

1.cryptography.hazmat.primitives.ciphers:
This module provides low-level cryptographic primitives such as AES and ChaCha20, which are essential for implementing secure encryption and decryption in custom applications. These ciphers offer flexibility and control, making them suitable for performance-critical security tasks.

![image](https://github.com/user-attachments/assets/95698393-28eb-44a0-aad5-c3ff464d122e)

2.time:
This module enables time-related operations such as tracking execution durations, introducing delays, and measuring performance benchmarks. It's often used in encryption systems to profile the speed and efficiency of algorithms.

3.psutil:
psutil is a cross-platform library used to monitor and retrieve real-time system and process-level metrics. It provides access to CPU usage, memory consumption, disk activity, and more—helpful for evaluating the resource usage of encryption algorithms.



4.PIL.Image (from the Pillow library):
The Pillow library extends image processing capabilities in Python. PIL.Image is used for opening, modifying, and saving image files, and is crucial in image encryption tasks where pixel-level access and transformations are required.

5.VS Code:
Visual Studio Code (VS Code) is a lightweight, open-source code editor widely used for developing and debugging Python-based encryption and data processing scripts due to its extensibility and integrated development tools.

6.MATLAB:
MATLAB is a high-level programming platform used for algorithm development, simulation, and mathematical modeling, particularly effective for analyzing chaotic maps and visualizing encryption behavior in controlled environments.
