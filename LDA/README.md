# Linear Discriminant Analysis (LDA) Project

This project demonstrates the application of **Linear Discriminant Analysis (LDA)** for dimensionality reduction and classification. The dataset used consists of facial images from the ORL dataset, and the project explores both a custom-designed LDA implementation and Python's built-in LDA function.

## Project Structure

- **`LDA_with_PCA.ipynb`**: The main Jupyter Notebook containing the code and explanations for the LDA analysis.
- **`ORL/`**: Directory containing subfolders of facial images for different individuals.

## Key Steps in the Notebook

1. **Import Libraries**:
   - Essential libraries such as `numpy`, `pandas`, `scikit-learn`, and `matplotlib` are imported.

2. **Data Loading and Preprocessing**:
   - Facial images are loaded from the `ORL` directory.
   - Images are flattened into vectors, and labels are encoded.
   - The dataset is split into training and testing sets.

3. **Principal Component Analysis (PCA)**:
   - PCA is applied to reduce the dimensionality of the dataset.
   - The explained variance ratio is analyzed to determine the optimal number of components.

4. **Custom LDA Implementation**:
   - A custom LDA class is implemented to compute class means, covariance matrices, and discriminant functions.
   - The model is trained and evaluated on the PCA-transformed data.

5. **Python's Built-in LDA**:
   - The `LinearDiscriminantAnalysis` class from `scikit-learn` is used for comparison.
   - The model is trained and evaluated on the PCA-transformed data.

6. **Dimensionality Analysis**:
   - The impact of varying the number of PCA components on LDA performance is analyzed.
   - Cross-validation is used to identify the optimal number of components.

7. **Results and Insights**:
   - The optimal dimensionality for PCA is found to be between 40 and 50 components.
   - Python's built-in LDA function achieves higher accuracy compared to the custom implementation.

## Dataset Description

The dataset consists of grayscale facial images organized into subfolders, where each subfolder represents a different individual. Images are preprocessed by flattening into vectors for analysis.

## Libraries Used

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `cv2`

## How to Run

1. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn opencv-python
2. Ensure the `ORL` directory is in the same folder as the notebook.
3. Open the `LDA_with_PCA.ipynb` file in Jupyter Notebook or any compatible IDE.
4. Run the cells sequentially to execute the analysis.

## Results

- The custom LDA implementation achieves an accuracy of approximately 85% with 45 PCA components.
- Python's built-in LDA function achieves an accuracy of approximately 95% with 50 PCA components.
- Excessive dimensionality reduction or increase negatively impacts model performance. 

## Author
    Mohammad Ali Etemadi Naeen