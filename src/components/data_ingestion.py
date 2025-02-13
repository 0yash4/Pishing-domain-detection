import os
import sys
from dataclasses import dataclass

import pandas as pd
from data_engineer import DataNormalization
from data_ingestion_config import DataIngestionConfig

from src.exception import CustomException
from src.logger import logging
from src.pipeline.model_trainer import model_training


@dataclass

class data_initailization:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the Data ingestion method or component")
        try:
            df=pd.read_csv('artifacts\dataset_full.csv')
            
            input_data = df.iloc[:, :-1]
            output_data = df.iloc[:, -1:]
            
            print("Input data shape:", input_data.shape)
            print("Output data shape:", output_data.shape)
            
            if input_data.shape[0] == output_data.shape[0]:
                input_data.to_csv(self.ingestion_config.input_data_path, index=False)
                output_data.to_csv(self.ingestion_config.output_data_path, index=False)
                
                logging.info("Ingestion of data is completed.")
            
            return(
                self.ingestion_config.input_data_path,
                self.ingestion_config.output_data_path,
            )
            
        except CustomException as e:
            raise CustomException(e, sys)
            

if __name__ == "__main__":
    obj=data_initailization()
    input_data_path, output_data = obj.initiate_data_ingestion()
    input_data = pd.read_csv(input_data_path)
    #data_norm = DataNormalization()
    #data_norm.save_normalized_data(input_data)
    #trainer = model_training()
    #trainer.model_trainer(input_data, output_data)
