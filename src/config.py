# src/config.py

# --- File Paths and Directories ---
INPUT_IMAGE_DIR = "data/input_images"
OUTPUT_DIR = "/data/inswapper_images"
MODEL_DIR = "models"
SWAPPER_MODEL_PATH = f"{MODEL_DIR}/inswapper_128.onnx"

# --- Model Configuration ---
FACE_ANALYZER_MODEL = "buffalo_l"

# --- Dataset Curation Parameters ---
IMAGES_PER_CATEGORY = 600 # This will generate 4 * 600 = 2400 total images
# Parameters for selecting similar/dissimilar pairs
SIMILAR_MAX_AGE_DIFF = 10
DISSIMILAR_MIN_AGE_DIFF = 15
