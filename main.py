import os
from PIL import Image

def convert_to_png(directory_path):
    for r, _, files in os.walk(directory_path):
        i = 0
        for file in files:
            filepath = os.path.join(r, file)
            try:
                img = Image.open(filepath)
                image_resized = img.resize((512, 512))
                image_resized.save(f'{os.path.splitext(filepath)[0]}.png')
                i += 1
                print(f"Converted {os.path.basename(filepath)} to PNG")
            except Exception as e:
                print(f"Error converting {os.path.basename(filepath)}: {e}")

# Example usage:
directory_path = "your_directory_path_here"
convert_to_png(directory_path)
