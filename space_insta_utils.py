from pathlib import Path
import requests
from PIL import Image
import urllib3
from os import path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_extension(user_url):
    return path.splitext(user_url)[1]


def crop_image(image_name):
    image = Image.open(image_name)
    if image.width > image.height:
        cropped_left = cropped_right = (image.width - image.height) / 2
        coordinates = (cropped_left, 0, image.width - cropped_right, image.height)
    else:
        cropped_up = cropped_down = (image.height - image.width) / 2
        coordinates = (0, cropped_up, image.width, image.height - cropped_down)
    crop = image.crop(coordinates)
    crop.save(image_name)


def save_image(image_url, images_dir, image_name_format):
    Path(images_dir).mkdir(parents=True, exist_ok=True)
    response = requests.get(image_url, verify=False)
    response.raise_for_status()
    image_name = '{}/{}'.format(images_dir, image_name_format)
    with open(image_name, 'wb') as file:
        file.write(response.content)
