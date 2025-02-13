import os
import sys
from dataclasses import dataclass


class DataIngestionConfig:
        raw_data_path = os.path.join("artifacts", "dataset_full.csv")
        input_data_path = os.path.join("artifacts", "input_data.csv")
        output_data_path = os.path.join("artifacts", "output_data.csv")