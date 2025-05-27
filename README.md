# Machine Learning Projects

This repository contains a collection of machine learning projects, each focusing on different algorithms and techniques. The projects are organized into separate directories, each with its own dataset, code, and documentation.

---

## Table of Contents

1. [Decision Tree](#decision-tree)
2. [Linear Discriminant Analysis (LDA)](#linear-discriminant-analysis-lda)
3. [Principal Component Analysis (PCA)](#principal-component-analysis-pca)
4. [Regression](#regression)
   - [Linear Regression](#linear-regression)
   - [Polynomial Regression](#polynomial-regression)
   - [Ridge & LASSO Regression](#ridge--lasso-regression)
5. [Spline Analysis](#spline-analysis)
6. [Support Vector Machines (SVM)](#support-vector-machines-svm)
7. [Housing Data Mining Price Prediction](#housing-data-mining-price-prediction)

---

## Decision Tree

- **Description**: A Decision Tree Classifier is implemented to predict the survival of passengers on the Titanic dataset.
- **Key Features**:
  - Data preprocessing and feature selection.
  - Hyperparameter tuning and cross-validation.
- **Files**:
  - `decision_tree.ipynb`: Jupyter Notebook containing the implementation.
  - `titanic.csv`: Dataset used for the analysis.
  - [README.md](Decision_Tree/README.md): Detailed documentation.

---

## Linear Discriminant Analysis (LDA)

- **Description**: Demonstrates the application of LDA for dimensionality reduction and classification using the ORL facial image dataset.
- **Key Features**:
  - Custom LDA implementation and comparison with Python's built-in LDA.
  - Integration with PCA for dimensionality reduction.
- **Files**:
  - `LDA.ipynb`: Jupyter Notebook containing the implementation.
  - `ORL/`: Directory containing the dataset.
  - [README.md](LDA/README.md): Detailed documentation.

---

## Principal Component Analysis (PCA)

- **Description**: Applies PCA to a diabetes dataset to reduce dimensionality and analyze feature contributions.
- **Key Features**:
  - Visualization of principal components.
  - Identification of influential features for diabetes prediction.
- **Files**:
  - `PCA.ipynb`: Jupyter Notebook containing the implementation.
  - `Diabetes.csv`: Dataset used for the analysis.
  - [README.md](PCA/README.md): Detailed documentation.

---

## Regression

### Linear Regression

- **Description**: Implements Linear Regression to predict car mileage using the Auto MPG dataset.
- **Key Features**:
  - Exploratory Data Analysis (EDA) and feature engineering.
  - Model training and evaluation.
- **Files**:
  - `Linear_Regression.ipynb`: Jupyter Notebook containing the implementation.
  - [README.md](Regression/Linear%20Regression/README.md): Detailed documentation.

### Polynomial Regression

- **Description**: Applies Polynomial Regression to predict real estate prices based on various features.
- **Key Features**:
  - Advanced diagnostics such as Cook’s distance and residual analysis.
  - Comparison of models with varying polynomial degrees.
- **Files**:
  - `real_estate.ipynb`: Jupyter Notebook containing the implementation.
  - `real_estate.csv`: Dataset used for the analysis.
  - [README.md](Regression/Polynomial%20Regression/README.md): Detailed documentation.

### Ridge & LASSO Regression

- **Description**: Explores Ridge and LASSO regression techniques for feature selection and regularization on the Boston Housing dataset.
- **Key Features**:
  - Dimensionality reduction with PCA.
  - Regularization parameter tuning using cross-validation.
- **Files**:
  - `Ridge_LASSO_Regression.ipynb`: Jupyter Notebook containing the implementation.
  - `Boston.csv`: Dataset used for the analysis.
  - [README.md](Regression/Ridge%20&%20LASSO%20Regression/README.md): Detailed documentation.

---

## Spline Analysis

- **Description**: Demonstrates regression techniques such as SplineTransformer, Polynomial Features, and Smoothing Splines on synthetic and real-world datasets.
- **Key Features**:
  - Case study on Bone Mineral Density (BMD) data.
  - Comparison of regression techniques based on performance metrics.
- **Files**:
  - `spline.ipynb`: Jupyter Notebook containing the implementation.
  - `Bone Mineral Density.csv`: Dataset used for the analysis.
  - [README.md](Spline/README.md): Detailed documentation.

---

## Support Vector Machines (SVM)

- **Description**: Implements SVM for classification tasks, including handwritten digit recognition and kernel-based classification.
- **Key Features**:
  - Robustness analysis against noise and rotation.
  - Hyperparameter tuning using GridSearchCV.
- **Files**:
  - `handwritten_digits_classification.ipynb`: Jupyter Notebook for digit classification.
  - `Data-hoda-full.mat`: Dataset used for the analysis.
  - [README.md](SVM/handwritten_digits_classification/README.md): Detailed documentation.

---

## Housing Data Mining Price Prediction

- **Description**: This project focuses on predicting housing prices using machine learning techniques. It includes data crawling, preprocessing, exploratory data analysis, and regression modeling to provide accurate price predictions based on features such as size, number of rooms, and location.
- **Key Features**:
  - Web crawling to collect housing data from online sources.
  - Data preprocessing and cleaning.
  - Exploratory data analysis (EDA) for insights.
  - Implementation of regression models for price prediction.
  - Model evaluation and performance metrics.
- **Files**:
  - `crawling_1.ipynb`: Notebook for scraping housing data links.
  - `crawling_2.ipynb`: Notebook for extracting detailed information from the links.
  - `Housing_Data_Mining_Price_Prediction.ipynb`: Notebook for data preprocessing, EDA, and regression modeling.
  - `House_Data.csv`: Dataset containing the cleaned housing data.
  - `updated_list.csv`: File containing the scraped housing data links.
  - `requirements.txt`: List of dependencies for the project.
  - `Dockerfile`: Docker configuration for running the project in a containerized environment.
- **Usage**:
  1. Run `crawling_1.ipynb` to scrape housing data links.
  2. Use `crawling_2.ipynb` to extract detailed information (price, size, number of rooms) from the links.
  3. Use `Housing_Data_Mining_Price_Prediction.ipynb` to preprocess the data, perform EDA, and train regression models.
  4. Optionally, use the `Dockerfile` to build and run the project in a containerized environment.

---

## Author
    Mohammad Ali Etemadi Naeen
