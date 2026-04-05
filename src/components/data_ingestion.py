import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

# Add project root to sys.path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    # Save artifacts in the project root folder
    train_data_path: str = os.path.join(os.getcwd(), 'artifacts', "train.csv")
    test_data_path: str = os.path.join(os.getcwd(), 'artifacts', "test.csv")
    raw_data_path: str = os.path.join(os.getcwd(), 'artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Load dataset
            df = pd.read_csv(r"C:\mlproject\notepad\data\StudentsPerformance.csv")
            logging.info("Read the dataset as dataframe")
            print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

            # Create artifacts folder in project root
            os.makedirs(os.path.join(os.getcwd(), "artifacts"), exist_ok=True)
            print(f"Artifacts folder path: {os.path.join(os.getcwd(), 'artifacts')}")

            # Save raw dataset
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved")

            # Train-test split
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train and test data saved successfully")

            print(f"Train CSV: {self.ingestion_config.train_data_path}")
            print(f"Test CSV: {self.ingestion_config.test_data_path}")

            logging.info("Ingestion of data completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()