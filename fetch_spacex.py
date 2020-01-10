import requests
import space_insta_utils

SPACEX_HOST = "https://api.spacexdata.com"
SX_VERSION = "v3"
IMAGES_DIR = 'images'
SPACEX_LAUNCH = 87


def fetch_spacex_one_launch(launch_number, images_dir):
    spacex_launches_url = "{}/{}/launches/{}".format(SPACEX_HOST, SX_VERSION, launch_number)
    response = requests.get(spacex_launches_url)
    response.raise_for_status()
    response = response.json()
    response = response.get("links")
    spacex_images_urls = response.get("flickr_images")
    for seqnum, spacex_image_url in enumerate(spacex_images_urls):
        seqnum += 1
        image_extension = space_insta_utils.get_extension(spacex_image_url)
        name_format = 'launch{}_spacex{n:02d}.{}'.format(launch_number, image_extension, n=seqnum)
        image_name = '{}/{}'.format(images_dir, name_format)
        space_insta_utils.save_image(spacex_image_url, images_dir, name_format)
        space_insta_utils.crop_image(image_name)


def main():
    fetch_spacex_one_launch(SPACEX_LAUNCH, IMAGES_DIR)


if __name__ == "__main__":
    main()
