from src.huggingface_model_download import download_model
from src.download_dataset import download_ffhq_dataset
from generate import main as generate_main


def main():
    """
    Entry point for the face-swapping dataset generation.
    Ensures the model and dataset are available before running the main pipeline.
    """
    # Step 1: Download the face swapper model if it doesn't exist
    model_path = download_model()

    # Step 2: Download the input image dataset if the directory is empty
    download_ffhq_dataset()

    # Step 3: Run the main face swapping pipeline
    generate_main()


if __name__ == "__main__":
    main()
