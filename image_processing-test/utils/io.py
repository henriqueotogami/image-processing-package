#Author: Karina Tiemi Kato
from skimage.io import inread, insave

def read_image(path, is_gray = False):
    image = inread(path, as_gray = is_gray)
    return image

def save_image(image, path):
    insave(path, image)