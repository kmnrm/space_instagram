import requests
import space_insta_utils

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


def fetch_hubble_image(image_id, images_dir):
    hubblesite_url = '{}/{}/image/{}'.format(HUBBLE_HOST, HUB_VERSION, image_id)
    response = requests.get(hubblesite_url)
    response.raise_for_status()
    response = response.json()
    hubble_images = response.get("image_files")
    hubble_image_url = [image_url['file_url'] for image_url in hubble_images][-1]
    hubble_image_url = 'http:{}'.format(hubble_image_url)
    image_extension = space_insta_utils.get_extension(hubble_image_url)
    name_format = 'hubble_{}{number}{}'.format(image_id, image_extension, number='')
    image_name = '{}/{}'.format(images_dir, name_format)
    space_insta_utils.save_image(hubble_image_url, images_dir, name_format)
    space_insta_utils.crop_image(image_name)


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
