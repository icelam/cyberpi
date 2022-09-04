#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Convert an image to a sprite matrix

Usage:
python image_to_sprite.py <filename>
"""

import os
import sys
from PIL import Image

class FileNotExistError(Exception):
    """Raised when image path provided as argument does not exists"""
    def __init__(self, filename):
        message = f'Unable to open {filename}. Please check if the file exists.'
        super().__init__(f'\033[91m{message}\033[0m')

class InvalidArgumentsError(Exception):
    """Raised when image path provided as argument does not exists"""
    def __init__(self):
        message = f'Invalid number of arguments. Usage: python {sys.argv[0]} <filename>'
        super().__init__(f'\033[91m{message}\033[0m')

def get_image_path():
    """Extract image path from arguments"""
    try:
        if len(sys.argv) != 2:
            raise InvalidArgumentsError()

        if not os.path.exists(sys.argv[1]):
            raise FileNotExistError(sys.argv[1])

        return sys.argv[1]
    except Exception as error: # pylint: disable=broad-except
        print(error)
        sys.exit(0)

def resize_image(file_path, size):
    """
    Resize image to requested size.
    As sprites are always square, image not having 1:1 ratio will be put to center of new image.
    """
    pillow_image = Image.open(file_path, 'r')
    pillow_image.thumbnail((size, size))

    background_color = (0, 0, 0)
    width, height = pillow_image.size

    # original ratio is 1:1, skip processing
    if width == height:
        return pillow_image

    # landscape image
    if width > height:
        square_pillow_image = Image.new(pillow_image.mode, (width, width), background_color)
        square_pillow_image.paste(pillow_image, (0, (width - height) // 2))
        return square_pillow_image

    # portrait image
    square_pillow_image = Image.new(pillow_image.mode, (height, height), background_color)
    square_pillow_image.paste(pillow_image, ((height - width) // 2, 0))
    return square_pillow_image

def rgb_to_hex(rgb):
    """Convert rgb tuple to hex string"""

    # remove alpha channel from PNG image
    if len(rgb) > 3:
        rgb = rgb[:(3 - len(rgb))]

    return '0x%02x%02x%02x' % rgb # pylint: disable=consider-using-f-string

def convert_to_color_matrix(pillow_image):
    """Convert pillow image data to list of hex string"""
    raw_data = list(pillow_image.getdata())
    matrix = [rgb_to_hex(rgb) for rgb in raw_data]
    return matrix

def save_to_file(output_directory, filename, data):
    """Write data to file"""
    output_path = f'{output_directory}/{filename}.txt'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    result_string = f'[{", ".join(map(str, data))}]'
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(result_string)

    print(f'\033[92mSprite matrix have been save to {output_path}\033[0m')

if __name__ == '__main__':
    image_path = get_image_path()
    image = resize_image(image_path, 16)
    rgb_list = convert_to_color_matrix(image)

    program_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.abspath(os.path.join(program_directory, os.pardir))

    save_to_file(
        os.path.join(parent_directory, 'sprite-matrix'),
        os.path.basename(image_path),
        rgb_list
    )
