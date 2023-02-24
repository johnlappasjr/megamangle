import os
from dotenv import load_dotenv
from PIL import Image
from multiprocessing import Pool
from tqdm import tqdm

load_dotenv('.env.path')

def resize_image(file_path):
    megapixels = 20
    if file_path.lower().endswith('.png'):
        with Image.open(file_path) as im:
            megapixels_in_pixels = megapixels * 1000000
            ratio = (megapixels_in_pixels / (im.width * im.height)) ** 0.5
            width = int(im.width * ratio)
            height = int(im.height * ratio)
            resized_im = im.resize((width, height))
            output_path = os.path.join(os.environ['OUTPUT_DIR'], os.path.relpath(file_path, os.environ['INPUT_DIR']))
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            resized_im.save(output_path)

def process_file(file_path):
    resize_image(file_path)
    return file_path

if __name__ == '__main__':
    input_dir = os.environ['INPUT_DIR']
    output_dir = os.environ['OUTPUT_DIR']
    pool = Pool(processes=6)
    file_paths = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    with tqdm(total=len(file_paths)) as pbar:
        for i, _ in enumerate(pool.imap_unordered(process_file, file_paths)):
            pbar.update()
    print("Done")