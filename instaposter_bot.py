from InstagramAPI import InstagramAPI
from PIL import Image

import os
import glob
import random

inst_api = InstagramAPI("__night.air", "kisunya2010")
inst_api.login()  # login

image_folder = "D:\\WK_DEV\\PY\\zerochan_parcer\\IMAGES\\"

def square(image):
    base = Image.open(image).convert('RGB')
    width, height = base.size
    size = max(width, height)

    # make a blank image for the text, initialized to transparent text color
    sqw = Image.new('RGB',(size, size), (255,255,255))

    center_x = 0
    center_y = 0

    if width < height:
        center_x = int(size/2 - width/2)
    else:
        center_y = int(size/2 - height/2)

    sqw.paste(base, (center_x, center_y))
    sqw.save(image)


def resize(image):
    img = Image.open(image)
    width, height = img.size
    size = max(width, height)
    k = 1
    if size >= 1080:
        k = 1080/size
        new_width = int(width * k)
        new_height = int(height * k)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(image)
    elif size <= 320:
        k = 320/size
        new_width = int(width * k)
        new_height = int(height * k)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(image)


def post():
    images = glob.glob(os.path.join(image_folder, "*.jpg"))
    img = images[random.randint(0, len(images) - 1)]
    resize(img)
    square(img)

    caption = "#kaito"
    inst_api.uploadPhoto(img, caption=caption)


def loop():
    while 1:
        now = datetime.now()
        if now.hour % 3 == 0:
            print(now.hour)
            post()
        time.sleep(60 * 60)

if __name__ == '__main__':
    post()
