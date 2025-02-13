import sys

import pandas as pd
from data_ingestion_config import DataIngestionConfig
from sklearn.preprocessing import normalize

from src.exception import CustomException
from src.logger import logging


class DataNormalization:
    """
    A class to handle data normalization operations on input datasets.
    """
    def __init__(self):
        self.exclude_columns = [
            'email_in_url', 'domain_in_ip', 'server_client_domain', 
            'tld_present_params', 'tls_ssl_certificate', 'url_google_index', 
            'domain_google_index', 'url_shortened', 'phishing'
        ]
        self.data_ingestion_config = DataIngestionConfig()
    
    def read_csv(self, input_data_path: str) -> pd.DataFrame:
        """
        Read CSV file from the given path
        
        Args:
            input_data_path (str): Path to the input CSV file
            
        Returns:
            pd.DataFrame: Loaded dataframe
        """
        try:
            return pd.read_csv(input_data_path)
        except Exception as e:
            logging.error(f"Error reading CSV file: {input_data_path}")
            raise CustomException(e, sys)

    def get_columns_index(self, df: pd.DataFrame, cols: list[str]) -> list[int]:
        """
        Get indices of specified columns in the dataframe
        
        Args:
            df (pd.DataFrame): Input dataframe
            cols (list[str]): List of column names to find indices for
            
        Returns:
            list[int]: List of column indices
        """
        try:
            idx_list = []
            for idx, col in enumerate(df.columns):
                if col in cols:
                    idx_list.append(idx)
            return idx_list
        except Exception as e:
            logging.error("Error getting column indices")
            raise CustomException(e, sys)

    def init_normalization(self, input_df: pd.DataFrame) -> pd.DataFrame:
        """
        Performs L1 normalization on specified columns of the input dataset.
        
        Args:
            input_df (pd.DataFrame): Input dataframe to normalize
            
        Returns:
            pd.DataFrame: Normalized dataframe
        """
        try:
            logging.info("Started Data Normalization")
            
            # Create a copy of input dataframe first
            df_normalized = input_df
            
            # Identify columns to normalize
            columns_to_not_normalize = self.get_columns_index(input_df, self.exclude_columns)
            
            logging.info(f"Normalizing {len(df_normalized)} columns")
            
            # Apply L1 normalization
            for idx in range(df_normalized.shape[1]):
                if idx in columns_to_not_normalize:
                    pass
                else:
                    df_normalized.iloc[:, idx:idx+1] = normalize(
                        df_normalized.iloc[:, idx:idx+1], 
                        norm='l1'
                    )
            
            logging.info("Data normalization completed successfully")
            
            return df_normalized
            
        except Exception as e:
            logging.error("Error in data normalization")
            raise CustomException(e, sys)
            
    def save_normalized_data(self, input_data: pd.DataFrame):
        """
        Saves the normalized data to the specified output path.
        
        Args:
            input_data (pd.DataFrame): Input data to normalize
        """
        try:
            logging.info("Starting to save normalized data")
            
            # Get normalized dataframe
            df_normalized = self.init_normalization(input_data)
            
            # Get the output path - assuming it's a string attribute now
            input_data_path = self.data_ingestion_config.input_data_path
            
            # Save to CSV
            df_normalized.to_csv(input_data_path, index=False)
            
            logging.info(f"Normalized data saved successfully to {input_data_path}")
            logging.info("\nFirst few rows of normalized data:")
            logging.info(f"\n{df_normalized.head()}")
            
            return df_normalized
            
        except Exception as e:
            logging.error("Error in saving normalized data")
            raise CustomException(e, sys)
        
    def predict_data_normalize(self):
        """
        Placeholder for prediction data normalization.
        """
        pass

if __name__ == "__main__":
    obj = DataNormalization()
    obj.save_normalized_data()