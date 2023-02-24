from PIL import Image
import os
from multiprocessing import Pool

def resize_image(file_path):
    megapixels = 20
    input_dir = 'path/to/input/directory'
    output_dir = 'path/to/output/directory'
    if file_path.lower().endswith('.png'):
        print(f"Resizing {file_path}")
        with Image.open(file_path) as im:
            megapixels_in_pixels = megapixels * 1000000
            ratio = (megapixels_in_pixels / (im.width * im.height)) ** 0.5
            width = int(im.width * ratio)
            height = int(im.height * ratio)
            resized_im = im.resize((width, height))
            output_path = os.path.join(output_dir, os.path.relpath(file_path, input_dir))
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            resized_im.save(output_path)
            print(f"Saved resized image to {output_path}")

if __name__ == '__main__':
    input_dir = 'path/to/input/directory'
    output_dir = 'path/to/output/directory'
    pool = Pool(processes=6) # Change the number of processes to suit your system
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            pool.apply_async(resize_image, args=(file_path,))
            print(f"Scheduled {file_path} for resizing")
    pool.close()
    pool.join()
    print("Done") 
