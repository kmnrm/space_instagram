# Space Instagram

Space Instagram downloads and crops images, and posts `.jpg`-images of hubble images collections and a certain SpaceX launch in your Instagram account.

### How to install
Use these steps before launching:
1. Create an Instagram account standard way (via Instagram Official App), if you do not have one. Signing up via browser may cause errors.
2. Create a `.env` file in `post_images.py` script directory and add your Instagram account login and password in the format below:
```
LOGIN=your_login
PASS=your_password
```
Do not use parenthesis, quotation marks or spaces, e.g:
```
LOGIN=john_doe_83232883
PASS=WhatAW0nderfu1DayToSignIn
```

Preinstall Python3 to use Space Instagram.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Getting started
There are three scripts to deal with:
1. `fetch_spacex.py` helps you get images from a certain SpaceX launch using public SpaceX API. 
The most current version of the API is `v3` with the following base URL `https://api.spacexdata.com/v3`. No authentication is required to use this public API. All the launch images are going to be downloaded to a new-created folder `images`. If the folder already exists, the images will be downloaded there without replacement.
If you want to get images from another SpaceX launch, change its number in the script (default value  - `87`):
```
SPACEX_LAUNCH = 87
IMAGES_DIR = 'images'

def main():
    fetch_spacex_one_launch(SPACEX_LAUNCH, IMAGES_DIR)
```
2. `fetch_hubble.py` helps you get images from [Hubblesite](http://hubblesite.org) collection of images using Hubblesite API. 
The most current version of the API is `v3` with the following base URL `http://hubblesite.org/api/v3`. No authentication is required to use this public API.
    There are six image collections presented in script as list:

    ```
    COLLECTIONS_NAMES = [
    'news',
    'wallpaper',
    'holiday_cards',
    'spacecraft',
    'printshop',
    'stsci_gallery'
    ]
    
    def main():
    collection_name = COLLECTIONS_NAMES[2] #collection 'holiday cards' has been chosen
    ```
    The collections differ from each other by image itself, its size and format. Try to download different collections to choose one you need.
    Advice: if you run into Internet connection and download speed issues, choose `Holiday cards` collection. Otherwise, it's gonna take some time to get the collection downloaded. 
    The images are to be named by their Hubblesite `image id` and to be downloaded to `images` new-created folder. If the folder already exists, the images will be downloaded there without replacement.

3. `post_images.py` helps you post downloaded `jpg`-images from `images` folder as an Instagram post in your Instagram account. The captions for each post are the same as images names. Be careful with posting too many photos as you may have no captions due to your Instagram account blocking (images will be posted though).

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).