import os
import pickle
import sys

import joblib
import numpy as np
import pandas as pd

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            joblib.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"❌ ERROR: File not found at {file_path}")
        raise CustomException("Pickle file not found", sys)
    except pickle.UnpicklingError:
        print("❌ ERROR: Corrupt or incompatible pickle file")
        raise CustomException("Pickle file corrupted", sys)
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        raise CustomException(e, sys)
    