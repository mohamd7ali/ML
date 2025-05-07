# PCA Project on Diabetes Dataset

This project demonstrates the application of Principal Component Analysis (PCA) on a diabetes dataset to reduce dimensionality and analyze the relationships between features. The dataset contains various attributes related to individuals' health and lifestyle, and the goal is to identify the most influential features for predicting diabetes.

## Project Structure

- **`PCA.ipynb`**: The main Jupyter Notebook containing the code and explanations for the PCA analysis.
- **`Diabetes.csv`**: The dataset used for the analysis, containing health and lifestyle attributes of individuals.

## Dataset Description

The dataset includes the following columns:

- **Age**: Age of the individual.
- **Sex**: Gender of the individual.
- **BloodPressure**: Blood pressure level.
- **GeneticRisk**: Genetic risk factor for diabetes.
- **BMI**: Body Mass Index.
- **PhysicalActivity**: Level of physical activity.
- **Married**: Marital status.
- **Work**: Employment type.
- **Smoker**: Smoking status.
- **Diabetes**: Target variable indicating whether the individual has diabetes (1) or not (0).

## Key Steps in the Notebook

1. **Data Preprocessing**:
   - Missing values are handled by replacing them with appropriate values (mean, median, or mode).
   - Numerical columns are standardized to have a mean of 0 and a standard deviation of 1 to ensure equal contribution to PCA.

2. **Exploratory Data Analysis (EDA)**:
   - Relationships between features are visualized using histograms, violin plots, and count plots.
   - Examples include:
     - Physical Activity vs. Work
     - Physical Activity vs. Diabetes
     - BMI vs. Marital Status
     - Smoking situations for men and women.

3. **Principal Component Analysis (PCA)**:
   - PCA is applied to the standardized numerical features to reduce dimensionality.
   - The cumulative explained variance is plotted to determine the number of components required to retain 90% of the variance.
   - The top 4 principal components are selected for further analysis.

4. **Visualization of PCA Results**:
   - A scatter plot of the first two principal components is created, with points colored based on diabetes status.
   - Feature contributions to the principal components are visualized using vectors in the PCA space.

5. **Insights**:
   - Features such as `BloodPressure`, `Age`, `BMI`, and `GeneticRisk` are identified as having a strong influence on diabetes prediction.
   - Longer vectors in the PCA space indicate stronger contributions of features to the principal components.

## Libraries Used

- `numpy`
- `pandas`
- `seaborn`
- `matplotlib`
- `scikit-learn`

## How to Run

1. Install the required libraries:
   ```bash
   pip install numpy pandas seaborn matplotlib scikit-learn

2. Open the PCA.ipynb file in Jupyter Notebook or any compatible IDE.

3. Run the cells sequentially to execute the analysis.

## Results
- PCA successfully reduced the dimensionality of the dataset while retaining 90% of the variance using 4 principal components.
- The scatter plot of the first two principal components shows clear separation between individuals with and without diabetes.
- The analysis highlights the most influential features for predicting diabetes.

## Author
    Mohammad Ali Etemadi Naeen
