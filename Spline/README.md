# Spline Analysis and Regression Techniques

This repository contains a Jupyter Notebook (`spline.ipynb`) that demonstrates various regression techniques, including **SplineTransformer**, **Polynomial Features**, and **Smoothing Splines**, to model and analyze data. The notebook also includes a case study on **Bone Mineral Density (BMD)** data, where these techniques are applied to predict `spnbmd` (spinal bone mineral density) based on age and gender.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Notebook Overview](#notebook-overview)
   - [Section 1: Sin(x) and Noise](#section-1-sinx-and-noise)
   - [Section 2: Piecewise Polynomial Splines](#section-2-piecewise-polynomial-splines)
   - [Section 3: Smoothing Splines](#section-3-smoothing-splines)
   - [Section 4: Bone Mineral Density Case Study](#section-4-bone-mineral-density-case-study)
3. [Results and Comparisons](#results-and-comparisons)
4. [Dependencies](#libraries-used-dependencies)
5. [How to Run](#how-to-run)
6. [Author](#author)

---

## Introduction

The notebook explores different regression techniques to model non-linear relationships in data. It starts with a simple example of modeling the `sin(x)` function with noise and progresses to a real-world dataset on bone mineral density. The goal is to compare the performance of different methods and identify the most suitable approach for the given data.

---

## Notebook Overview

### **Section 1: Sin(x) and Noise**:
This section generates a noisy sin(x) function and demonstrates how to model it using different regression techniques:

- SplineTransformer:
    - Fits B-splines to the data.
    - Visualizes the relationship between the number of knots, degree, and flexibility of the splines.

- Polynomial Features:
    - Fits polynomial regression models of varying degrees.
    - Compares the performance of polynomial regression with splines.

- Gaussian Features:
    - Uses Gaussian basis functions to model the data.
    - Compares the performance with other methods.

### **Section 2: Piecewise Polynomial Splines**:
This section demonstrates how to construct **piecewise polynomial splines** using the `symfit` library. It includes:
- Defining polynomial segments for different ranges of `x`.
- Applying continuity, first derivative, and second derivative constraints to ensure smooth transitions between segments.
- Comparing the performance of models with varying levels of constraints.

### **Section 3: Smoothing Splines**:
This section introduces **smoothing splines** using the `csaps` library. It includes:
- Exploring the effect of the smoothing parameter (`p`) on the fit.
- Calculating the Mean Squared Error (MSE) for training and testing data for different values of `p`.
- Selecting the optimal smoothing parameter based on performance metrics.

### **Section 4: Bone Mineral Density Case Study**
This section applies the regression techniques to a real-world dataset on **Bone Mineral Density (BMD)**. The dataset includes columns for `age`, `gender`, and `spnbmd`. Key steps include:
- Data Preprocessing:
    - Handling missing values.
    - Splitting the data by gender.
    - Scaling the features using `StandardScaler`.

- Ridge Regression with Polynomial Features:
    - Uses `GridSearchCV` to find the optimal polynomial degree and regularization parameter (`alpha`).
    - Evaluates the model's performance using MSE and R² metrics.

- Ridge Regression with SplineTransformer:
    - Fits cubic splines to the data.
    - Compares the performance with polynomial regression.

- Smoothing Splines:
    - Finds the optimal smoothing parameter (`p`) for males and females.
    - Evaluates the model's performance using MSE and R² metrics.


---

## Results and Comparisons

The notebook evaluates the performance of three regression techniques: **Polynomial Features**, **SplineTransformer**, and **Smoothing Splines**. The results are compared based on their flexibility, robustness, interpretability, and computational complexity.

### Key Findings:

1. **Sin(x) Example**:
   - **SplineTransformer** provided the best fit with the lowest Mean Squared Error (MSE) on both training and testing data.
   - **Polynomial Features** performed well but showed signs of overfitting for higher degrees.
   - **Gaussian Features** had the highest MSE and were less effective for this dataset.

2. **Bone Mineral Density (BMD) Case Study**:
   - **Smoothing Splines** achieved the best performance, especially for noisy data, by providing a smooth and flexible fit.
   - **Ridge Regression with Polynomial Features** was effective but required careful tuning of the polynomial degree and regularization parameter.
   - **Ridge Regression with SplineTransformer** offered a balance between flexibility and interpretability, outperforming polynomial regression in most cases.

### Comparison of Methods:

| **Criteria**            | **Polynomial Features**                  | **SplineTransformer**                  | **Smoothing Splines**                  |
|--------------------------|------------------------------------------|-----------------------------------------|-----------------------------------------|
| **Flexibility**          | Limited by polynomial degree            | High, with adjustable knots and degree | Very high, smooth fit to noisy data    |
| **Robustness**           | Sensitive to outliers                   | Moderate robustness                    | Highly robust to noise                 |
| **Interpretability**     | Decreases with higher polynomial degree | Moderate                               | Moderate                               |
| **Computational Cost**   | High for higher degrees                 | Moderate                               | Low to moderate                        |

### Performance Metrics:

#### Sin(x) Example:
- **SplineTransformer**:
  - MSE (Training): 0.0527
  - MSE (Testing): 0.0428
- **Polynomial Features**:
  - MSE (Training): 0.0583
  - MSE (Testing): 0.0447
- **Gaussian Features**:
  - MSE (Training): 0.0526
  - MSE (Testing): 0.0456

#### BMD Case Study:
- **Smoothing Splines**:
  - Best smoothing parameter (`p`) for males and females resulted in the lowest MSE and highest R² values.
- **Ridge Regression with Polynomial Features**:
  - Required careful tuning of polynomial degree and regularization parameter (`alpha`) using `GridSearchCV`.
- **Ridge Regression with SplineTransformer**:
  - Achieved competitive results with fewer hyperparameters to tune.

### Conclusion:
- For the **Sin(x)** example, **SplineTransformer** is the best choice due to its flexibility and low MSE.
- For the **BMD dataset**, **Smoothing Splines** provided the best overall performance, especially for noisy data.
- **Polynomial Features** are suitable for simpler relationships but may overfit for higher degrees.

---

## Libraries Used (Dependencies)

The following Python libraries are required to run the notebook:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scipy`
- `sklearn`
- `symfit`
- `csaps`
- `IPython`
- `cv2`

To install the required libraries, run the following commands:

```bash
!pip install csaps
!pip install symfit
```
---

## How to Run

1. Install the required libraries.

2. Open the `spline.ipynb` file in Jupyter Notebook or any compatible IDE.

3. Run the cells sequentially to execute the analysis.

---

## Author
    Mohammad Ali Etemadi Naeen

