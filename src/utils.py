import os
import pickle
import sys

import joblib
import numpy as np
import pandas as pd

from src.exception import CustomException

print("Checking pickle file existence:", os.path.exists(pkl_file_path))


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            joblib.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(f"Error saving object: {str(e)}", sys)
    
def load_object(file_path):
    """
    Load a serialized object from a file using joblib.

    Args:
        file_path (str): Path to the joblib file.

    Returns:
        object: The loaded object (e.g., a trained model).
    
    Raises:
        CustomException: If the file is corrupted or not found.
    """
    try:
        if not os.path.exists(file_path):
            raise CustomException(f"File not found: {file_path}")

        with open(file_path, "rb") as file:
            obj = joblib.load(file)  # Load object using joblib
        return obj

    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        raise CustomException(f"Error loading object: {str(e)}", sys)
    