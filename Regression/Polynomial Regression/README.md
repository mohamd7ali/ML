# Polynomial Regression on Real Estate Dataset

This project demonstrates the application of **Polynomial Regression** on a real estate dataset to predict house prices based on various features. The dataset contains information about real estate transactions, including house age, distance to the nearest MRT station, number of convenience stores, and geographical coordinates.

## Project Structure

- **`real_estate.ipynb`**: The main Jupyter Notebook containing the code and explanations for the regression analysis.
- **`real_estate.csv`**: The dataset used for the analysis, containing real estate transaction details.

## Dataset Description

The dataset includes the following columns:

- **No**: Index or ID of the transaction.
- **X1 transaction date**: Transaction date (floating-point representation of the year).
- **X2 house age**: Age of the house in years.
- **X3 distance to the nearest MRT station**: Distance to the nearest MRT station in meters.
- **X4 number of convenience stores**: Number of convenience stores within walking distance.
- **X5 latitude**: Latitude of the property.
- **X6 longitude**: Longitude of the property.
- **Y house price of unit area**: Target variable indicating the house price per unit area.

## Key Steps in the Notebook

1. **Data Loading and Exploration**:
   - The dataset is loaded into a Pandas DataFrame.
   - Summary statistics, missing values, and distributions of features are analyzed.

2. **Preprocessing**:
   - The `No` column is dropped as it is not relevant for prediction.
   - Missing values are handled appropriately.
   - Features are standardized to ensure equal contribution to the regression model.

3. **Exploratory Data Analysis (EDA)**:
   - Histograms and pair plots are used to visualize feature distributions and relationships.
   - Correlation and covariance matrices are computed to identify relationships between features and the target variable.

4. **Variance Inflation Factor (VIF)**:
   - VIF is calculated to detect multicollinearity among predictors.
   - Features with high VIF values are considered for removal or transformation.

5. **Polynomial Regression**:
   - Polynomial features of varying degrees are generated.
   - Models are trained on the training set and evaluated on validation and test sets.
   - Performance metrics such as MSE, RMSE, R², and F-statistic are computed.

6. **Advanced Diagnostics**:
   - Cook’s distance is used to identify influential data points.
   - Residuals are analyzed for normality using Q–Q plots and the Shapiro–Wilk test.
   - Partial F-tests are performed to compare nested models.

7. **Discussion of Theoretical Concepts**:
   - Topics such as Cochran’s theorem, multicollinearity, and F-statistics are discussed to provide theoretical insights.

## Libraries Used

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `statsmodels`

## How to Run

1. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn statsmodels

2. Open the real_estate.ipynb file in Jupyter Notebook or any compatible IDE.

3. Run the cells sequentially to execute the analysis.

## Results
- Polynomial regression models of varying degrees were trained and evaluated.
- The analysis highlights the importance of features such as X3 distance to the nearest MRT station and X4 number of convenience stores in predicting house prices.
- Advanced diagnostics such as Cook’s distance and residual analysis were performed to ensure model reliability.

## Author
    Mohammad Ali Etemadi Naeen
   