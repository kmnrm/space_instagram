import os
from instabot import Bot
from dotenv import load_dotenv

IMAGES_DIR = 'images'


def main():
    load_dotenv()
    login = os.getenv("LOGIN")
    password = os.getenv("PASS")
    images = os.listdir(IMAGES_DIR)
    jpg_images = list(filter(lambda x: x.endswith('.jpg'), images))
    bot = Bot()
    bot.login(username=login, password=password)

    for jpg_image in jpg_images:
        try:
            jpg_image_name = '{}/{}'.format(IMAGES_DIR, jpg_image)
            caption = jpg_image.split('.')[0]
            bot.upload_photo(jpg_image_name, caption=caption)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
        except RuntimeError:
            continue


if __name__ == "__main__":
    main()
