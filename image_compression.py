import cv2
import matplotlib.pyplot as plt
import os
print("Image compression Tool")
# Load the image (change the file name to your image)
img_path = "project2.jpg"
image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Show original image
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')
plt.show()
print(f"Original Size: {os.path.getsize(img_path) / 1024:.2f} KB")

# Compress the image
output_path = 'compressed_image.jpg'
cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR), [int(cv2.IMWRITE_JPEG_QUALITY), 30])

# Show compressed image
compressed_image = cv2.imread(output_path)
compressed_image = cv2.cvtColor(compressed_image, cv2.COLOR_BGR2RGB)

plt.imshow(compressed_image)
plt.title("Compressed Image (Quality=30)")
plt.axis('off')
plt.show()
print(f"Compressed Size: {os.path.getsize(output_path) / 1024:.2f} KB")
