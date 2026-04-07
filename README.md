# ML Project - Student Performance Prediction

A comprehensive machine learning project for predicting student performance using various regression models. This project implements end-to-end ML pipeline with data preprocessing, model training, and deployment using Flask.

## 🚀 Features

- **Data Preprocessing**: Automated feature engineering with scaling and encoding
- **Multiple Models**: Support for Random Forest, CatBoost, XGBoost, and other regression models
- **Model Evaluation**: Comprehensive evaluation with R² scores and cross-validation
- **Web Interface**: Flask-based web application for predictions
- **Modular Architecture**: Well-structured codebase with separate components
- **Logging & Error Handling**: Robust logging and custom exception handling
- **Jupyter Notebooks**: Interactive notebooks for EDA and model experimentation

## 📋 Requirements

- Python 3.8+
- scikit-learn
- pandas
- numpy
- flask
- catboost
- xgboost
- matplotlib
- seaborn

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mlproject
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## 📊 Usage

### Training the Model

Run the training pipeline:
```bash
python src/pipeline/train_pipeline.py
```

This will:
- Load and preprocess the data
- Train the model
- Save artifacts (model.pkl, preprocessor.pkl) in the `artifacts/` directory

### Running the Web Application

Start the Flask application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Using Jupyter Notebooks

Explore the notebooks in the `notepad/` directory:
- `EDA.ipynb` - Exploratory Data Analysis
- `MODEL TRAINING.ipynb` - Model training experiments

## 📁 Project Structure

```
mlproject/
├── artifacts/                 # Model artifacts and data
│   ├── data.csv              # Training data
│   ├── model.pkl             # Trained model
│   └── preprocessor.pkl      # Data preprocessor
├── notepad/                   # Jupyter notebooks
│   ├── EDA.ipynb             # Exploratory Data Analysis
│   ├── MODEL TRAINING.ipynb  # Model training notebook
│   └── data/                 # Notebook data
├── src/                      # Source code
│   ├── components/           # ML pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/             # Training and prediction pipelines
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── exception.py          # Custom exception handling
│   ├── logger.py             # Logging configuration
│   └── utils.py              # Utility functions
├── templates/                # Flask HTML templates
│   ├── home.html
│   └── index.html
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
└── README.md                 # Project documentation
```

## 🧪 Model Details

### Supported Algorithms
- Random Forest Regressor
- CatBoost Regressor
- XGBoost Regressor
- Other scikit-learn regressors

### Evaluation Metrics
- R² Score
- Cross-validation scores
- Training vs Test performance

### Data Preprocessing
- Standard scaling for numerical features
- One-hot encoding for categorical features
- Handling missing values and outliers

## 🔧 Configuration

### Data Configuration
- **Data Path**: `artifacts/data.csv`
- **Target Column**: `math score` (configurable)
- **Features**: Student demographics and preparation data

### Model Configuration
- **Random Forest**: 100 estimators, random_state=42
- **Hyperparameter Tuning**: GridSearchCV with 3-fold CV

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

For questions or support, please open an issue in the repository.

## 🔄 Future Enhancements

- [ ] Add more regression algorithms
- [ ] Implement model comparison dashboard
- [ ] Add API endpoints for batch predictions
- [ ] Include feature importance analysis
- [ ] Add model monitoring and retraining pipeline