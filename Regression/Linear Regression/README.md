# Linear Regression Project

This project demonstrates the implementation of a Linear Regression model using Python and various data science libraries. The dataset used in this project is the Auto MPG dataset, which is processed and analyzed to predict the Miles Per Gallon (MPG) of cars based on various features.

## Project Structure

- **`Linear_Regression.ipynb`**: The main Jupyter Notebook containing the code and explanations for the Linear Regression analysis.
- **Dataset**: The dataset is fetched from the UCI Machine Learning Repository and saved locally as `DataSet.csv`.

## Key Steps in the Notebook

1. **Dataset Preparation**:
   - The dataset is downloaded from the UCI repository.
   - Missing values in the `Horsepower` column are handled by replacing them with the mean value.

2. **Exploratory Data Analysis (EDA)**:
   - Pair plots and scatter plots are used to analyze the relationships between features and the target variable (`MPG`).
   - A heatmap is generated to visualize feature correlations.

3. **Feature Engineering**:
   - One-hot encoding is applied to the `Car Name` column to extract car brands.
   - Highly correlated features (`Cylinders` and `Displacement`) are optionally removed to analyze their impact on the model.

4. **Model Training**:
   - A Linear Regression model is trained using the `scikit-learn` library.
   - The model's coefficients and intercept are calculated.

5. **Model Evaluation**:
   - The Mean Squared Error (MSE) and R-squared values are computed to evaluate the model's performance.
   - Scatter plots are used to compare actual vs. predicted values.

6. **Feature Impact Analysis**:
   - The impact of removing highly correlated features on the model's performance is analyzed.

## Libraries Used

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

## Results

- The Linear Regression model performs well, with a low MSE and a high R-squared value.
- Removing highly correlated features increases the MSE, indicating that these features are important for the model's accuracy.

## How to Run

1. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn

2. Open the Linear_Regression.ipynb file in Jupyter Notebook or any compatible IDE.

3. Run the cells sequentially to execute the analysis.

## Author
    Mohammad Ali Etemadi Naeen
