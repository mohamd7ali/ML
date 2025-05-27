# Housing Data Mining Price Prediction

This project focuses on predicting housing prices using machine learning techniques. It includes data crawling, preprocessing, exploratory data analysis, and regression modeling to provide accurate price predictions based on features such as size, number of rooms, and location.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Notebooks](#notebooks)
- [Dependencies](#libraries-used-dependencies)
- [Author](#author)

---

## Project Overview

The goal of this project is to predict housing prices by leveraging data mining and machine learning techniques. The project includes web crawling to collect data, preprocessing to clean and prepare the data, and machine learning models to analyze and predict housing prices.

---

## Features

- Web crawling to collect housing data from online sources.
- Data preprocessing and cleaning.
- Exploratory data analysis (EDA) for insights.
- Implementation of regression models for price prediction.
- Model evaluation and performance metrics.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Housing_Data_Mining_Price_Prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Housing_Data_Mining_Price_Prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Crawling Data
1. Run the `crawling_1.ipynb` notebook to scrape housing data links.
2. Use the `crawling_2.ipynb` notebook to extract detailed information (price, size, number of rooms) from the links.

### Data Preprocessing and Modeling
1. Use the `Housing_Data_Mining_Price_Prediction.ipynb` notebook to:
   - Preprocess the data.
   - Perform exploratory data analysis.
   - Train and evaluate regression models.

### Running the Docker Container (Optional)
1. Build the Docker image:
   ```bash
   docker build -t housing-price-prediction .
   ```
2. Run the container:
   ```bash
   docker run -p 8888:8888 housing-price-prediction
   ```

---

## Libraries Used (Dependencies)

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Selenium
- BeautifulSoup
- Googletrans

---

## Dataset

The dataset is collected using web crawling and contains features such as:
- Price
- Meters (size of the property)
- Number of Rooms

The dataset is saved as `House_Data.csv` after preprocessing.

---

## Notebooks

### `crawling_1.ipynb`
- Crawls housing data links from the website.
- Saves the links to `updated_list.csv`.

### `crawling_2.ipynb`
- Extracts detailed information (price, size, number of rooms) from the links.
- Saves the cleaned data to `Final_Data.csv`.

### `Housing_Data_Mining_Price_Prediction.ipynb`
- Preprocesses the data.
- Performs exploratory data analysis (EDA).
- Implements regression models for price prediction.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## Author
    Mohammad Ali Etemadi Naeen
