from .captions import get_random_caption
from .images import get_random_image  

def generate_meme():
    caption = get_random_caption()
    image_path = get_random_image()  # Now gets local image path
    return f"🎉 MEME GENERATED 🎉\nImage: {image_path}\nCaption: {caption}"

# def generate_meme():
#     caption = get_random_caption()
#     image_path = get_random_image()
#     return caption  # Only return the caption now