import requests
import numpy as np
from PIL import Image

random_url = "https://www.random.org/integers/"

row_pixels = 128
column_pixels = 128
total_pixels = row_pixels * column_pixels #total size:128x128

def get_ints(num):
    params = {
        'num': str(num), #Number of integers to be generated
        'min': '0', #Least value of integer
        'max': '255', #Maximum value of integer
        'col': '3', #Number of columns to arrange integers. we use 3 for Red, Blue and Green
        'base': '10', #Decimal numbers
        'format': 'plain', #plain text document
        'rnd': 'new' #new randomization
    }

    result = requests.get(random_url, params=params)
    if result.status_code == 200:
        print "success"
    else:
        print(" Error")
        exit()
    return [int(x) for x in result.text.split()] #split and convert string to integer

def rgb_pixels():
    pixels = []
    total_rgb_pixels = total_pixels * 3

    while total_rgb_pixels > 0:
        if (total_rgb_pixels > 10000):
            pixels.extend(get_ints(10000)) #only 10000 integers can be generated
        else:
            pixels.extend(get_ints(total_rgb_pixels))
        total_rgb_pixels -= 10000

    return pixels

def create_image(random_pixels):
    img = Image.new('RGB', (128, 128))  # create new image
    rgb_pixel = np.array(random_pixels).reshape((row_pixels * column_pixels, 3))
    img.putdata([tuple(pixel) for pixel in rgb_pixel]) #add pixels to image
    img.save("image.bmp")
    print("Image Created")

def main():
    random_rgb_pixels = rgb_pixels()
    create_image(random_rgb_pixels)

# execute
main()
