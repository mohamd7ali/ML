# Decision Tree Classifier on Titanic Dataset

This project demonstrates the use of a **Decision Tree Classifier** to predict the survival of passengers on the Titanic. The dataset used is the Titanic dataset, which contains information about passengers such as age, gender, class, and whether they survived or not. The notebook explores data preprocessing, feature selection, hyperparameter tuning, and model evaluation using techniques like k-fold cross-validation.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset Description](#dataset-description)
3. [Key Steps in the Notebook](#key-steps-in-the-notebook)
4. [Libraries Used](#libraries-used)
5. [How to Run](#how-to-run)
6. [Results](#results)
7. [Author](#author)

---

## Introduction

The Titanic dataset is a classic dataset used for binary classification tasks. The goal of this project is to predict whether a passenger survived the Titanic disaster based on features such as age, gender, class, and fare. A **Decision Tree Classifier** is used to build the predictive model, and various techniques like hyperparameter tuning and cross-validation are applied to improve the model's performance.

---

## Dataset Description

The dataset used in this project is the Titanic dataset, which contains the following columns:

- **Survived**: Target variable (1 = survived, 0 = did not survive).
- **Pclass**: Passenger class (1 = first, 2 = second, 3 = third).
- **Name**: Name of the passenger.
- **Sex**: Gender of the passenger.
- **Age**: Age of the passenger.
- **Siblings/Spouses Aboard**: Number of siblings/spouses aboard the Titanic.
- **Parents/Children Aboard**: Number of parents/children aboard the Titanic.
- **Fare**: Ticket fare.

---

## Key Steps in the Notebook

1. **Data Import and Exploration**:
   - Load the Titanic dataset using Pandas.
   - Explore the dataset for missing values, data types, and basic statistics.
   - Visualize correlations and relationships between features using heatmaps and pair plots.

2. **Data Preprocessing**:
   - Handle missing values and irrelevant features.
   - Convert categorical variables (e.g., `Sex`) into numerical format using one-hot encoding.
   - Drop irrelevant features such as `Name`, `Siblings/Spouses Aboard`, and `Parents/Children Aboard`.

3. **Feature Selection**:
   - Separate the dataset into features (`X`) and target (`y`).
   - Remove irrelevant features to improve model performance.

4. **Model Training**:
   - Train a **Decision Tree Classifier** using Scikit-learn.
   - Perform hyperparameter tuning using **GridSearchCV** to find the best parameters for the model.

5. **Model Evaluation**:
   - Evaluate the model using metrics like accuracy.
   - Use **k-fold cross-validation** (k=10) to assess the model's performance on different subsets of the data.
   - Compare results with and without hyperparameter tuning.

6. **Insights and Observations**:
   - Analyze the impact of hyperparameters like `criterion`, `max_depth`, and `min_samples_split` on model performance.
   - Discuss the trade-offs between bias and variance.

---

## Libraries Used

The following Python libraries are required to run the notebook:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

---

## How to Run

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```
2. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```
3. Open the `decision_tree.ipynb` file in Jupyter Notebook or any compatible IDE.
4. Run the cells sequentially to execute the analysis.

---

## Results

### Baseline Decision Tree
- **Accuracy on the test set**: ~70% (varies depending on the random seed and train-test split).
- The baseline model was trained without hyperparameter tuning, providing a starting point for comparison.

### Hyperparameter Tuning
- **Best Parameters** (found using GridSearchCV):
  - `criterion`: Gini or entropy.
  - `max_depth`: Optimal depth for the dataset.
  - `min_samples_split`: Minimum samples required to split a node.
  - `min_samples_leaf`: Minimum samples required to be a leaf node.
  - `max_features`: Number of features to consider when looking for the best split.
- **Accuracy on the test set after tuning**: ~75% (varies depending on the dataset split).
- Hyperparameter tuning improved the model's performance by optimizing the decision tree's structure.

### Cross-Validation
- **K-Fold Cross-Validation (k=10)**:
  - Mean accuracy across 10 folds: ~74% (varies depending on the random seed).
  - Cross-validation provided a more robust estimate of the model's performance by evaluating it on multiple subsets of the data.

### Insights
- Hyperparameter tuning significantly improved the model's accuracy compared to the baseline.
- The use of k-fold cross-validation ensured that the model's performance was not overly dependent on a single train-test split.
- The trade-offs between bias and variance were analyzed by adjusting parameters like `max_depth` and `min_samples_split`.

---

## Author
    Mohammad Ali Etemadi Naeen
