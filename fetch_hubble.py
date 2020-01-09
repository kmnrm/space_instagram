from pathlib import Path
import requests
from PIL import Image
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HUBBLE_HOST = "http://hubblesite.org/api"
HUB_VERSION = "v3"
IMAGES_DIR = 'images'
COLLECTIONS_NAMES = [
    'news',
    'wallpaper',
    'holiday_cards',
    'spacecraft',
    'printshop',
    'stsci_gallery'
    ]


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
    response = requests.get(image_url, verify=False)
    response.raise_for_status()
    image_name = '{}/{}'.format(images_dir, image_name_format)
    with open(image_name, 'wb') as file:
        file.write(response.content)


def fetch_hubble_image(image_id, images_dir):
    hubblesite_url = '{}/{}/image/{}'.format(HUBBLE_HOST, HUB_VERSION, image_id)
    response = requests.get(hubblesite_url)
    response.raise_for_status()
    response = response.json()
    hubble_images = response.get("image_files")
    hubble_image_url = [image_url['file_url'] for image_url in hubble_images][-1]
    hubble_image_url = 'http:{}'.format(hubble_image_url)
    image_extension = get_extension(hubble_image_url)
    name_format = 'hubble_{}{number}.{}'.format(image_id, image_extension, number='')
    image_name = '{}/{}'.format(images_dir, name_format)
    save_image(hubble_image_url, images_dir, name_format)
    crop_image(image_name)


def main():
    collection_name = COLLECTIONS_NAMES[2]
    hubble_collection_url = '{}/{}/images/{}'.format(HUBBLE_HOST, HUB_VERSION, collection_name)
    response = requests.get(hubble_collection_url)
    response.raise_for_status()
    response = response.json()
    image_ids = [image_id['id'] for image_id in response]

    for image_id in image_ids:
        fetch_hubble_image(image_id, IMAGES_DIR)


if __name__ == "__main__":
    main()
