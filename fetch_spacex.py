from pathlib import Path
import requests
from PIL import Image

SPACEX_HOST = "https://api.spacexdata.com"
SX_VERSION = "v3"
IMAGES_DIR = 'images'
SPACEX_LAUNCH = 87


def get_extension(user_url):
    url_extension = user_url.split('.')[-1]
    return url_extension


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
    response = requests.get(image_url)
    response.raise_for_status()
    image_name = '{}/{}'.format(images_dir, image_name_format)
    with open(image_name, 'wb') as file:
        file.write(response.content)


def fetch_spacex_one_launch(launch_number, images_dir):
    spacex_launches_url = "{}/{}/launches/{}".format(SPACEX_HOST, SX_VERSION, launch_number)
    response = requests.get(spacex_launches_url)
    response.raise_for_status()
    response = response.json()
    response = response.get("links")
    spacex_images_urls = response.get("flickr_images")
    for seqnum, spacex_image_url in enumerate(spacex_images_urls):
        seqnum += 1
        image_extension = get_extension(spacex_image_url)
        name_format = 'launch{}_spacex{n:02d}.{}'.format(launch_number, image_extension, n=seqnum)
        image_name = '{}/{}'.format(images_dir, name_format)
        save_image(spacex_image_url, images_dir, name_format)
        crop_image(image_name)


def main():
    fetch_spacex_one_launch(SPACEX_LAUNCH, IMAGES_DIR)


if __name__ == "__main__":
    main()
