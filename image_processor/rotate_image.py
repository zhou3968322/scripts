import sys
import os
from PIL import Image

img_dir = sys.argv[1]
out_dir = sys.argv[2]
for img_name in os.listdir(img_dir):
    img_path = os.path.join(img_dir, img_name)
    img = Image.open(img_path)
    new_img_path = os.path.join(out_dir, img_name.rsplit('.', 1)[0] + '_rotate.' +  img_name.rsplit('.', 1)[1])
    img.rotate(270).save(new_img_path)

