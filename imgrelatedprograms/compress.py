from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r"C:\python_project1\project1\Luffy vs admirals.jpg").convert("RGB")
arr = np.array(img)

plt.imshow(arr)
plt.axis("off")
plt.title("Original Image")
plt.show()

def compress_image(arr, block_size=8):
    h, w, c = arr.shape
    compressed = arr.copy()

    for i in range(0, h, block_size):
        for j in range(0, w, block_size):
            block = arr[i:i+block_size, j:j+block_size, :]
            avg_color = block.mean(axis=(0, 1))
            compressed[i:i+block_size, j:j+block_size, :] = avg_color

    return compressed.astype(np.uint8)

compressed = compress_image(arr, 8)
plt.imshow(compressed)
plt.axis("off")
plt.title("Compressed Image")
plt.show()

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(arr)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(compressed)
plt.title("Compressed")
plt.axis("off")

plt.show()




