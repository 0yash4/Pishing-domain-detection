import os
import sys
from dataclasses import dataclass


class DataIngestionConfig:
        raw_data_path = os.path.join("artifacts", "dataset_full.csv")
        input_data_path = os.path.join("artifacts", "input_data.csv")
        output_data_path = os.path.join("artifacts", "output_data.csv")
        pkl_file_path = os.path.join("artifacts", "model.pkl")
        


if __name__ == "__main__":

        di = DataIngestionConfig()
        pkl_file_path = di.pkl_file_path
        print("Checking pickle file existence:", os.path.exists(pkl_file_path))
