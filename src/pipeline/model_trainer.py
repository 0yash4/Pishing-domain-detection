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
class model_trainer_config:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    

class model_training:
    def __init__(self):
        self.model_trainer_config = model_trainer_config()
        
    def model_trainer(self, input_data, output_data):
        try:
            input_data = pd.read_csv(input_data)
            output_data = pd.read_csv(output_data)
        
            models = {
                "Random Forest": RandomForestClassifier(),
                }

            # Define hyperparameters to search over for each model
            param_grid = {
                "Random Forest": {'n_estimators': [200], 'max_depth': [None], 'min_samples_split': [2]},
                }
            
            results = {}
            for name, model in models.items():
                print(f"Training {name}...")
                grid_search = GridSearchCV(estimator=model, param_grid=param_grid[name], cv=5, scoring='accuracy')
                grid_search.fit(input_data, output_data)
                best_params = grid_search.best_params_
                best_model = grid_search.best_estimator_
                #feature_name = model.get_feature_names_out()
                accuracy = cross_val_score(best_model, input_data, 
                                           output_data, cv=5, scoring='accuracy').mean()
                results[name] = {'accuracy': accuracy, 'best_params': best_params}
                            
            if accuracy < 0.6:
                raise CustomException("No best model found")
            else:
                logging.info(f"Best model found with the accuracy score of {accuracy}")
                #logging.info(f"Columns = {feature_name}")
            
            save_object(
                self.model_trainer_config.trained_model_file_path,
                best_model
            )
            
            return(
                accuracy
            )   
                     
        except CustomException as e:
            raise CustomException(e, sys)
            
        