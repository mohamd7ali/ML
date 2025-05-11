# Support Vector Machine (SVM) Project

This project demonstrates the application of **Support Vector Machines (SVM)** for classification tasks using various kernel functions. The notebook explores linear SVM, polynomial SVM, and radial basis function (RBF) SVM, providing insights into their behavior and hyperparameter tuning.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Key Steps in the Notebook](#key-steps-in-the-notebook)
4. [Libraries Used](#libraries-used)
5. [How to Run](#how-to-run)
6. [Results](#results)
7. [Author](#author)

---

## Introduction

Support Vector Machines (SVM) are powerful supervised learning algorithms used for classification and regression tasks. This project focuses on using SVM for binary classification with different kernel functions to handle both linearly and non-linearly separable data. The notebook provides a hands-on approach to understanding SVM concepts, including margin maximization, support vectors, and the role of hyperparameters like `C` and `gamma`.

---

## Project Structure

- **`SVM_Kernels.ipynb`**: The main Jupyter Notebook containing the code and explanations for the SVM analysis.
- **`plots.py`**: Helper functions for visualizing decision boundaries, margins, and support vectors.
- **`helpers.py`**: Utility functions for generating toy datasets used in the notebook.
- **Datasets**: Synthetic datasets generated programmatically using Scikit-learn.

---

## Key Steps in the Notebook

1. **Introduction to SVM**:
   - Overview of SVM and its optimization formulation.
   - Explanation of key concepts like margin maximization, support vectors, and the role of the regularization parameter `C`.

2. **Linear SVM**:
   - Implementation of a linear SVM classifier using Scikit-learn's `SVC` class.
   - Visualization of decision boundaries, margins, and support vectors.
   - Exploration of the effect of varying the `C` parameter on the margin and decision boundary.

3. **Kernel SVM**:
   - Introduction to kernel functions and their role in transforming data into higher-dimensional spaces.
   - Implementation of polynomial and RBF kernels for non-linearly separable data.
   - Comparison of explicit polynomial feature expansion with the kernel trick.

4. **Hyperparameter Tuning**:
   - Exploration of the effect of hyperparameters like `C`, `degree`, and `gamma` on the decision boundary and model performance.
   - Visualization of decision boundaries for different hyperparameter values.

5. **Insights and Observations**:
   - Discussion on the differences between polynomial feature expansion and polynomial kernel functions.
   - Analysis of the impact of hyperparameters on model complexity and generalization.

---

## Libraries Used

The following Python libraries are required to run the notebook:

- `numpy`
- `matplotlib`
- `scikit-learn`

---

## How to Run

1. Install the required libraries:
   ```bash
   pip install numpy matplotlib scikit-learn
2. Open the `SVM_Kernels.ipynb` file in Jupyter Notebook or any compatible IDE.
3. Run the cells sequentially to execute the analysis.

---

## Results

- **Linear SVM**:
  - Successfully demonstrated the concept of margin maximization and the role of support vectors.
  - Showed how the `C` parameter affects the margin and decision boundary.
  - Observed that higher `C` values result in narrower margins, while lower `C` values allow for wider margins with some misclassifications.

- **Polynomial SVM**:
  - Compared explicit polynomial feature expansion with the kernel trick.
  - Highlighted the effect of the polynomial degree on the decision boundary.
  - Observed that higher polynomial degrees increase model complexity, capturing more intricate decision boundaries.

- **RBF SVM**:
  - Explored the impact of the `gamma` parameter on the decision boundary.
  - Observed that higher `gamma` values result in more localized decision boundaries, while lower `gamma` values lead to smoother, more generalized boundaries.

- **General Observations**:
  - The choice of kernel and hyperparameters (`C`, `degree`, `gamma`) significantly affects the model's performance and complexity.
  - Validation data is essential for selecting the best kernel and hyperparameters in real-world applications.
  - SVM with kernel functions effectively handles non-linearly separable data by transforming it into higher-dimensional spaces.

---

## Author
    Mohammad Ali Etemadi Naeen