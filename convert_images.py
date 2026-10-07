from PIL import Image
import os

images = ["lukhach.png", "star.png", "phapsu.png", "king.png"]

for img_name in images:
    if os.path.exists(img_name):
        try:
            img = Image.open(img_name)
            webp_name = img_name.replace(".png", ".webp")
            # Convert RGBA to RGB for webp if necessary, but webp supports transparency
            img.save(webp_name, "WEBP", quality=80)
            print(f"Converted {img_name} to {webp_name}")
        except Exception as e:
            print(f"Failed to convert {img_name}: {e}")
    else:
        print(f"File {img_name} not found")
