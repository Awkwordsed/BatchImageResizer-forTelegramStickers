import os
from PIL import Image

im = "yourPath"

for r, _, files in os.walk(im):
    i = 0
    for file in files:
        filepath = os.path.join(r, file)
        try:
            img = Image.open(filepath)
            image_resized = img.resize((512, 512))
            image_resized.save(f'test_{i}.png')
            i = i + 1
            print(i)
        except Exception as e:
            print(f"Error opening {filepath}: {e}")