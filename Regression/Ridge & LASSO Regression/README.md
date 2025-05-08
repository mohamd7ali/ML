# Linear Regression and Feature Selection on Boston Housing Dataset

This project demonstrates the application of **Linear Regression**, **Feature Selection**, and **Dimensionality Reduction** techniques on the Boston Housing dataset to predict house prices based on various features. The notebook explores multiple regression techniques, including Ridge and Lasso regression, and evaluates their performance.

## Project Structure

- **`Ridge_LASSO_Regression.ipynb`**: The main Jupyter Notebook containing the code and explanations for the regression analysis and feature selection.
- **`Boston.csv`**: The dataset used for the analysis, containing housing data with features such as crime rate, number of rooms, and tax rate.

## Dataset Description

The dataset includes the following columns:

- **CRIM**: Per capita crime rate by town.
- **ZN**: Proportion of residential land zoned for lots over 25,000 sq. ft.
- **INDUS**: Proportion of non-retail business acres per town.
- **CHAS**: Charles River dummy variable (1 if tract bounds river; 0 otherwise).
- **NX**: Nitric oxides concentration (parts per 10 million).
- **RM**: Average number of rooms per dwelling.
- **AGE**: Proportion of owner-occupied units built prior to 1940.
- **DIS**: Weighted distances to five Boston employment centers.
- **RAD**: Index of accessibility to radial highways.
- **TAX**: Full-value property-tax rate per $10,000.
- **PTRATIO**: Pupil-teacher ratio by town.
- **B**: 1000(Bk - 0.63)^2 where Bk is the proportion of Black residents by town.
- **LSTAT**: % lower status of the population.
- **MEDV**: Median value of owner-occupied homes in $1000s (target variable).

## Key Steps in the Notebook

1. **Data Loading and Exploration**:
   - The dataset is loaded into a Pandas DataFrame.
   - Summary statistics, missing values, and data types are analyzed.

2. **Exploratory Data Analysis (EDA)**:
   - Correlation heatmaps and pair plots are used to visualize relationships between features and the target variable (`MEDV`).
   - Features such as `LSTAT`, `RM`, and `PTRATIO` are identified as having strong correlations with `MEDV`.

3. **Linear Regression**:
   - A linear regression model is trained on the dataset.
   - Coefficients and intercepts are calculated, and the model's performance is evaluated using metrics such as Mean Squared Error (MSE) and R².

4. **Feature Selection**:
   - Forward selection is implemented iteratively and using the `SequentialFeatureSelector` from `scikit-learn`.
   - The top 3 features (`LSTAT`, `RM`, and `PTRATIO`) are selected based on their predictive power.

5. **Dimensionality Reduction with PCA**:
   - Principal Component Analysis (PCA) is applied to reduce the dataset's dimensionality.
   - The explained variance ratio is analyzed, and the first three principal components are visualized in 3D.

6. **Regularization Techniques**:
   - **Ridge Regression**:
     - The effect of the regularization parameter (`alpha`) on coefficients and MSE is analyzed.
     - The optimal `alpha` is determined using cross-validation.
   - **Lasso Regression**:
     - The sparsity-inducing property of Lasso is demonstrated by analyzing the number of non-zero coefficients as `alpha` increases.
     - The optimal `alpha` is determined using cross-validation.

7. **Model Comparison**:
   - The performance of Linear Regression, Ridge Regression, and Lasso Regression is compared using R² scores across varying training set sizes.
   - The relationship between the training set ratio and the optimal `alpha` for Ridge and Lasso is analyzed.

## Libraries Used

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

## How to Run

1. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn

2. Open the Ridge_LASSO_Regression.ipynb file in Jupyter Notebook or any compatible IDE.

3. Run the cells sequentially to execute the analysis.

## Results
- **Linear Regression**:
   - Identified LSTAT, RM, and PTRATIO as the most important features for predicting house prices.
   - Achieved a reasonable R² score, but prone to overfitting with high-dimensional data.

- **Ridge Regression**:
   - Reduced overfitting by penalizing large coefficients.
   - Performed well with small datasets but showed diminishing returns with larger datasets.

- **Lasso Regression**:
   - Induced sparsity by setting some coefficients to zero, effectively performing feature selection.
   - Performed comparably to Ridge Regression but with fewer features.

- **PCA**:
   - Reduced the dataset to three principal components while retaining most of the variance.
   - Highlighted trade-offs between computational efficiency and predictive accuracy.

## Author
    Mohammad Ali Etemadi Naeen