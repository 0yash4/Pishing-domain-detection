import os
import pickle
import sys
from dataclasses import dataclass

import dill
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import (GridSearchCV, cross_val_score,
                                     train_test_split)
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTraining:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def model_trainer(self, input_data, output_data):
        try:
            # Load input & output data
            input_data = pd.read_csv(input_data)
            output_data = pd.read_csv(output_data)
        
            models = {
                "Random Forest": RandomForestClassifier(),
            }

            param_grid = {
                "Random Forest": {'n_estimators': [200], 'max_depth': [None], 'min_samples_split': [2]},
            }
            
            best_model = None
            best_accuracy = 0
            
            for name, model in models.items():
                print(f"Training {name}...")
                grid_search = GridSearchCV(estimator=model, param_grid=param_grid[name], cv=5, scoring='accuracy')
                grid_search.fit(input_data, output_data)
                
                accuracy = cross_val_score(grid_search.best_estimator_, input_data, output_data, cv=5, scoring='accuracy').mean()
                
                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_model = grid_search.best_estimator_
                    
            if best_model is None or best_accuracy < 0.6:
                raise CustomException("No suitable model found with accuracy >= 0.6")
            else:
                logging.info(f"Best model found with an accuracy score of {best_accuracy}")

            save_object(
                self.model_trainer_config.trained_model_file_path,
                best_model
            )
            
            return best_accuracy

        except Exception as e:
            raise CustomException(f"Error in model training: {str(e)}", sys)
            
        