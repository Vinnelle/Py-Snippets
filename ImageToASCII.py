#!/usr/bin/env python3

"""
Image To ASCII converter
"""

from PIL import Image, ImageSequence
import sys

def main():
    """
    Main function
    """
    name = input("Enter File Name With Extension: ")
    # Open the GIF file
    try:
        img = Image.open(name)
    except IndexError:
        print("Please specify a GIF file!")
        sys.exit(1)
    except IOError as err:
        print(err)
        sys.exit(1)

    # Get image size and convert to grayscale
    width, height = img.size
    img = img.convert('L')

    # Create ASCII characters
    ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    num_chars = len(ascii_chars)

    # Convert image to ASCII characters
    text = ""
    for y in range(0, height):
        for x in range(0, width):
            gray = img.getpixel((x, y))
            text += ascii_chars[int((gray / 255.0) * num_chars)]
        text += "\n"

    # Save ASCII image
    with open("ascii_image_" + name + ".txt", "w") as f:
        f.write(text)

if __name__ == '__main__':
    main()
