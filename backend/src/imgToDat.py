import math
import numpy as np
from PIL import Image
# import math


def compressedImg(filePath, augment=0):
    img = Image.open(filePath)
    width, height = img.size

    # calculate gcd value of image to resize original image

    # imgCompressed = img.resize((146, 96))
    imgCompressed = img.resize((400, 400))
    # imgCompressed.save('compressed.png', 'png')

    if augment == -1:
        return np.array(list(img.getdata())).reshape(-1)
    else:
        return np.array(list(imgCompressed.getdata())).reshape(-1)


def restoreImg(decrypted, file_name, dimSize=(400,400)):

    # temp = [np.uint8(i) for i in decrypted]

    width = dimSize[0]
    height = dimSize[1]
    temp = np.array(decrypted).reshape((height, width, 3))

    imgRecovered = Image.fromarray(temp)
    imgRecovered.save(file_name, format='png')


def encrypt_to_disk_as_image(encrypted_data):
    encrypted_data = encrypted_data
    img_data = np.array([item for sublist in encrypted_data for item in sublist])
    img_size = int(len(img_data)**0.5)  # Determine the size of the image
    img_data = np.resize(img_data, (img_size, img_size))

    # Normalize data to the 0-255 range if necessary
    img_data = (img_data - np.min(img_data)) / (np.max(img_data) - np.min(img_data)) * 255
    img_data = img_data.astype(np.uint8)

    # Create and save the image
    img = Image.fromarray(img_data, 'L')  # 'L' for grayscale, use 'RGB' for color images
    img.save('static/encrypted_image.png')  # Save as PNG

# if __name__ == '__main__':
#     compressedImg('space.jpg', 2)
#     restoreImg('data.txt', 'height_and_width.txt')
