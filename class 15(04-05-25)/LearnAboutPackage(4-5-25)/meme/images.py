import os
import random
from pathlib import Path

def get_random_image():
    # Get the path to the images folder
    images_dir = Path(__file__).parent / "images"
    
    # List all image files
    image_files = [f for f in os.listdir(images_dir) 
                  if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        raise ValueError("No images found! Please add images to meme/images folder")
    
    # Return full path to a random image
    return str(images_dir / random.choice(image_files))