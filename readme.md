

# Diamond Price Prediction
-----
## Introduction

This project aims to predict the price of a diamond based on various features such as carat weight, cut quality, color, clarity, and other dimensions. The goal is to perform regression analysis to estimate the diamond's price using these characteristics.

## Dataset Information

### Independent Variables:
1. **id**: Unique identifier for each diamond.
2. **carat**: Carat weight of the diamond. Carat (ct.) is the unique unit of weight measurement used exclusively for gemstones and diamonds.
3. **cut**: Quality of the diamond cut (e.g., Fair, Good, Very Good, Premium, Ideal).
4. **color**: Color grade of the diamond, with values ranging from D (best) to J (worst).
5. **clarity**: Clarity of the diamond, a measure of the stone's purity and rarity, graded by the visibility of characteristics under 10x magnification.
6. **depth**: The depth of the diamond as a percentage of the width (Depth = Z / average(X, Y) * 100).
7. **table**: The width of the diamond's table expressed as a percentage of its average diameter.
8. **x**: Length of the diamond (in millimeters).
9. **y**: Width of the diamond (in millimeters).
10. **z**: Height of the diamond (in millimeters).

### Target Variable:
- **price**: Price of the diamond in USD.

### Dataset Source:
The dataset used in this project can be found on Kaggle: [Diamond Price Dataset](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)

## Project Structure

```plaintext
.
├── artifacts
│   ├── train.csv
│   ├── test.csv
├── notebooks
│   ├── EDA.ipynb
│   ├── Model_Training.ipynb
├── src
│   ├── components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipelines
│   │   ├── training_pipeline.py
│   │   ├── prediction_pipeline.py
├── application.py
├── setup.py
├── requirements.txt
├── README.md
└── venv/
```

- **data/**: Contains the training and testing datasets.
- **notebooks/**: Contains the Jupyter notebooks for exploratory data analysis (EDA) and model training.
- **src/components/**: Contains Python modules for data ingestion, data transformation, and model training.
- **src/pipelines/**: Contains the training and prediction pipelines.
- **app.py**: The main Flask application script.
- **setup.py**: Script for packaging and distribution.
- **requirements.txt**: List of dependencies needed to run the project.
- **README.md**: This file.
- **venv/**: The virtual environment directory.

## Setup and Run Instructions

### 1. Clone the Repository
```bash
git clone [Your GitHub Repository URL]
cd [Your Project Directory]
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install the Required Packages
```bash
pip install -r requirements.txt
```

### 5. Run the Flask Application
```bash
python application.py
```

### 6. Access the Application
Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with the application.

### 7. Deactivate the Virtual Environment (Optional)
When done, you can deactivate the virtual environment with:
```bash
deactivate
```

## Model Training

The model training pipeline includes several regression algorithms, with the following performance metrics on the training data:

1. **Linear Regression**
   - RMSE: 1013.90
   - MAE: 674.03
   - R² Score: 93.69%
   
2. **Lasso Regression**
   - RMSE: 1013.88
   - MAE: 675.07
   - R² Score: 93.69%
   
3. **Ridge Regression**
   - RMSE: 1013.91
   - MAE: 674.06
   - R² Score: 93.69%
   
4. **ElasticNet Regression**
   - R² Score: 85.56%

## Future Work
- Explore additional feature engineering techniques.
- Implement advanced hyperparameter tuning.
- Deploy the model using a more scalable solution.

---
