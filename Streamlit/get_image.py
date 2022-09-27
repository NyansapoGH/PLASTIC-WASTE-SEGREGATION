import os

from PIL import Image

PATH_TO_TEST_IMAGES = 'C://Users/NYANSAPO/Desktop/Mini Project/test_images'  #Change directory to fit your work


def get_list_of_images():
    file_list = os.listdir(PATH_TO_TEST_IMAGES)
    return [str(filename) for filename in file_list if str(filename).endswith('.jpg')]


def get_opened_image(image):
    return Image.open(image)
