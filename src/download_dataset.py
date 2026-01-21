import os
from tqdm import tqdm
from src import config
from datasets import load_dataset

# Number of images to download
NUM_IMAGES = 2000
DATASET_NAME = "marcosv/ffhq-dataset"


def download_ffhq_dataset():
    """
    Downloads a subset of the FFHQ dataset from Hugging Face if the input directory is empty.
    This is designed to run inside the Docker container at startup.
    """
    input_dir = config.INPUT_IMAGE_DIR

    os.makedirs(input_dir, exist_ok=True)

    # Check if the directory already contains the required number of images
    num_existing_images = len(os.listdir(input_dir))
    if num_existing_images >= NUM_IMAGES:
        print(f"[INFO] Input directory '{input_dir}' already contains {num_existing_images} images. Skipping dataset download.")
        return

    print(f"[INFO] Found {num_existing_images} images, which is less than the required {NUM_IMAGES}. Downloading dataset from '{DATASET_NAME}'...")

    try:
        # These libraries are installed in the Dockerfile
        from datasets import load_dataset

        # Load the dataset streamingly to avoid downloading the whole ~25GB dataset
        dataset = load_dataset(DATASET_NAME, split="train", streaming=True)

        # Take the first NUM_IMAGES
        subset = dataset.take(NUM_IMAGES)

        for i, example in enumerate(tqdm(subset, total=NUM_IMAGES, desc="Downloading images")):
            image = example["image"]
            # Ensure image is in RGB format for saving as JPG
            if image.mode != "RGB":
                image = image.convert("RGB")
            image_path = os.path.join(input_dir, f"ffhq_{i:05d}.jpg")
            image.save(image_path)

        print(f"\n[INFO] Successfully downloaded {NUM_IMAGES} images to '{input_dir}'.")
    except Exception as e:
        print(f"[ERROR] Failed to download dataset: {e}")
        raise