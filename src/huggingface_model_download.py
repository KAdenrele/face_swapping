import os
import subprocess
from . import config


def download_model():
    """
    Checks if the model exists and downloads it using curl if necessary.
    Returns the path to the model.
    """
    model_path = config.SWAPPER_MODEL_PATH
    model_dir = os.path.dirname(model_path)

    # Create model directory if it doesn't exist
    os.makedirs(model_dir, exist_ok=True)

    if not os.path.exists(model_path):
        print(f"[INFO] Swapper model not found at {model_path}.")
        print("[INFO] Downloading inswapper_128.onnx model using curl...")

        url = "https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/inswapper_128.onnx?download=true"

        command = ["curl", "-L", url, "-o", model_path]

        try:
            subprocess.run(command, check=True)
            print(f"\n[INFO] Model downloaded successfully to {model_path}")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to download model using curl: {e}")
            if os.path.exists(model_path):
                os.remove(model_path)
            raise RuntimeError("Failed to download model") from e
        except FileNotFoundError:
            print("[ERROR] `curl` command not found. Please install curl and make sure it is in your PATH.")
            raise
    else:
        print(f"[INFO] Swapper model already exists at {model_path}.")

    return model_path