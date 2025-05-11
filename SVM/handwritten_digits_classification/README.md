# Number Classification Using SVM
This project demonstrates the use of **Support Vector Machines (SVM)** in classifying handwritten digits. It covers the complete workflow—from reading and preprocessing the image data to training various SVM models and evaluating their performance. The dataset used contains grayscale images of handwritten digits. In addition, the project investigates the robustness of these models against noise and rotational distortions. 

---

## Table of Contents
- [Project Structure](#project-structure)
- [Dataset Description](#dataset-description)
- [Key Steps in the Notebook](#key-steps-in-the-notebook)
- [Libraries Used](#libraries-used)
- [How to Run](#how-to-run)
- [Results](#results)
- [Author](#author)

---

## Project Structure

- **`handwritten_digits_classification.ipynb`**: The main Jupyter Notebook containing the code and explanations for the SVM-based number classification.
- **Dataset**: The dataset is loaded from a `.mat` file (`Data-hoda-full.mat`) containing grayscale images and their corresponding labels.

---

## Dataset Description

The dataset consists of grayscale images of handwritten digits. Each image is labeled with its corresponding digit (0-9). The dataset is preprocessed to ensure uniform dimensions and flattened for compatibility with SVM classifiers.

---

## Key Steps in the Notebook

1. **Import Libraries**:
   - Essential libraries such as `numpy`, `scikit-learn`, `matplotlib`, and `cv2` are imported.

2. **Data Loading and Preprocessing**:
   - The dataset is loaded from a `.mat` file.
   - Images are resized using symmetric padding to ensure uniform dimensions.
   - Images are flattened into vectors for compatibility with SVM classifiers.

3. **Train-Test Split**:
   - The dataset is split into training (70%) and testing (30%) sets using `train_test_split`.

4. **SVM Classifier**:
   - Two multiclass classification strategies are implemented:
     - **One-vs-One (OvO)**: Fits one classifier per class pair.
     - **One-vs-All (OvA)**: Fits one classifier per class against all other classes.
   - Various kernel functions (`linear`, `rbf`, `poly`, `sigmoid`) are explored.

5. **Hyperparameter Tuning**:
   - The regularization parameter `C` is tuned using `GridSearchCV` to find the optimal value for each kernel.

6. **Robustness Analysis**:
   - **Noise Robustness**:
     - Salt-and-pepper noise is added to the test set to evaluate the classifier's robustness.
   - **Rotation Robustness**:
     - Test images are rotated by 30 degrees using different interpolation methods (`INTER_NEAREST`, `INTER_LINEAR`, `INTER_CUBIC`, `INTER_LANCZOS4`) to analyze the impact on accuracy.

7. **Results and Observations**:
   - The accuracy of the SVM classifier is evaluated for different kernels, noise levels, and rotation angles.
   - Insights into the robustness of SVM to noise and rotation are discussed.

---

## Libraries Used

The following Python libraries are required to run the notebook:

- `numpy`
- `scikit-learn`
- `matplotlib`
- `cv2`
- `scipy`
- `seaborn`
- `skimage`

To install the required libraries, run the following command:

```bash
pip install numpy scikit-learn matplotlib opencv-python scipy seaborn scikit-image
```

---

## How to Run

1. Install the required libraries using the command above.
2. Ensure the dataset file (`Data-hoda-full.mat`) is available in the specified path.
3. Open the `handwritten_digits_classification.ipynb` file in Jupyter Notebook or any compatible IDE.
4. Run the cells sequentially to execute the analysis.

---

## Results

- The **RBF kernel** achieved the highest accuracy among all kernels.
- The classifier's accuracy significantly dropped when salt-and-pepper noise was added to the test set, indicating low robustness to noise.
- Rotating the test images reduced accuracy to approximately 18%, showing that the dataset is not robust to rotation.

---

## Author
    Mohammad Ali Etemadi Naeen
