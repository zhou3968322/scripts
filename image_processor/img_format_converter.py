from PIL import Image
import sys
input_file = sys.argv[1]
new_file_path = sys.argv[2]
img = Image.open(input_file)
img.save(new_file_path, 'JPEG', quality=100)
