from PIL import Image
import os

# Set the desired size in megapixels
megapixels = 20

# Set the input and output directories
input_dir = '/Users/someuser/Desktop/images/'
output_dir = '/Users/someuser/Desktop/output/'

# Iterate through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a PNG
    if filename.lower().endswith('.png'):
        # Open the image
        img_path = os.path.join(input_dir, filename)
        with Image.open(img_path) as im:
            # Calculate the desired size in pixels
            megapixels_in_pixels = megapixels * 1000000
            ratio = (megapixels_in_pixels / (im.width * im.height)) ** 0.5
            width = int(im.width * ratio)
            height = int(im.height * ratio)
            # Resize the image
            resized_im = im.resize((width, height))
            # Save the resized image in the output directory
            output_path = os.path.join(output_dir, filename)
            resized_im.save(output_path)
