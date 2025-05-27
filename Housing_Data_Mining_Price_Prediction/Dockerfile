# FROM python:3

# # Install Jupyter Notebook
# RUN pip install jupyter

# # Copy the .ipynb file into the container
# COPY requirements.txt /app/
# COPY Housing_Data_Mining_Price_Prediction.ipynb /workspace/Housing_Data_Mining_Price_Prediction.ipynb

# # Set the working directory to the copied location
# WORKDIR /workspace

# # Command to run Jupyter Notebook
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# Use the official Python image as a base
FROM python

# Copy necessary files into the container
COPY requirements.txt /app/
COPY House_Data.csv /app/
# COPY Housing_Data_Mining_Price_Prediction.py /app/

# Set the working directory
WORKDIR /app

# Install required dependencies
RUN pip install -r requirements.txt

# Command to run the Python code
CMD ["python3", "Housing_Data_Mining_Price_Prediction.py"]
