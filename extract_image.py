#!/usr/bin/python3

from PIL import Image
import numpy as np
import re

def get_pixel_matrix(image):

    print(image.size, len(list(image.getdata())))

    data = image.getdata()

    image_array = np.asarray(data, np.dtype('int,int,int,int'))

    return image_array.reshape(image.size)

def resize_image(image, size=None, height=None, width=None):
    """
        Either define size, height or width:
            defining size, resizes it to any tuple (width, height) input.
            defining height or width will maintain aspect ratio and resize the dimension specified
    """

    if size != None and (height != None and width != None):

        raise TooManyArguments

    elif size == None and (height == None and width == None):

        raise NotEnoughArguments

    if height and width: raise TooManyArguments

    if size == None:

        size = scale_aspect_ratio(image.size, height or width, width!=None)

    print(size)

    image = image.resize(size, Image.ANTIALIAS)

    return image

def scale_aspect_ratio(original_size, new_dimension, is_width=True):
    """
        original_size is the original dimensions (width, height) of the image to scale
        new_dimension is an int: the new size of the image in pixels
                       (or) str: the scale to be multiplied by 'x2', 'x1.5'
        is_width defines whether the dimension to change is the width or height
    """

    axis = 0 if is_width else 1

    scale = None

    if "x" in str(new_dimension):

        scale = float(re.search(r'x\d?.*\d', str(new_dimension)).group())

        new_dimension = original_size[axis] * scale

    if scale == None: scale = new_dimension / original_size[axis]

    new_size = (new_dimension, int(original_size[1-axis]*scale))

    if not is_width: new_size = new_size[::-1]

    return new_size

img = Image.open('dome.png')
rgb_img = img.convert('RGB')

img = resize_image(img, width=10)

img.show()

print(get_pixel_matrix(img))
