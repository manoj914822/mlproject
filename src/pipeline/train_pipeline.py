import os
import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
import pickle

from src.exception import CustomException
from src.utils import save_object  # function to save model/preprocessor


class TrainPipeline:
    def __init__(self, data_path: str, target_column: str):
        # Get the project root directory (parent of parent of this script)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(script_dir))
        
        # Make data_path absolute if it's relative
        if not os.path.isabs(data_path):
            self.data_path = os.path.join(project_root, data_path)
        else:
            self.data_path = data_path
            
        self.target_column = target_column
        self.artifacts_dir = os.path.join(project_root, "artifacts")
        os.makedirs(self.artifacts_dir, exist_ok=True)

    def run_pipeline(self):
        try:
            # 1️⃣ Load the data
            df = pd.read_csv(self.data_path)

            # 2️⃣ Split features and target
            X = df.drop(self.target_column, axis=1)
            y = df[self.target_column]

            # 3️⃣ Identify column types
            categorical_cols = X.select_dtypes(include=["object", "string"]).columns.tolist()
            numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

            # 4️⃣ Create preprocessing pipeline
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num", StandardScaler(), numerical_cols),
                    ("cat", OneHotEncoder(sparse_output=False, handle_unknown='ignore'), categorical_cols)
                ]
            )

            # 5️⃣ Transform features
            X_scaled = preprocessor.fit_transform(X)

            # 6️⃣ Train model
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_scaled, y)

            # 7️⃣ Save artifacts
            save_object(os.path.join(self.artifacts_dir, "preprocessor.pkl"), preprocessor)
            save_object(os.path.join(self.artifacts_dir, "model.pkl"), model)

            print("Training completed. Artifacts saved in 'artifacts/' directory.")

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    data_path = "artifacts/data.csv"  # your training CSV
    target_column = "math score"  # your target
    pipeline = TrainPipeline(data_path, target_column)
    pipeline.run_pipeline()