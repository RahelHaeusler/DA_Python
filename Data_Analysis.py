#inspiraton https://www.kaggle.com/code/janiobachmann/bank-marketing-campaign-opening-a-term-deposit/notebook

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_csv(file_path):
    # Read the CSV file into a pandas DataFrame with semicolon as delimiter
    df = pd.read_csv(file_path, delimiter=';')

    # Display the first few rows of the DataFrame
    print("First few rows of the data:")
    print(df.head())

    # Display basic statistics of numerical columns
    print("\nBasic statistics of numerical columns:")
    print(df.describe())

    # Display information about the DataFrame including data types and null values
    print("\nInformation about the DataFrame:")
    print(df.info())

    # Count missing values per column
    missing_values_count = df.isnull().sum()
    print("\nNumber of missing values per column:")
    print(missing_values_count)

    # Additional analysis
    # Iterate over object (string) columns and print unique values
    for col in df.select_dtypes(include='object').columns:
        print(f"\nUnique values in column '{col}':")
        print(df[col].unique())




# Provide the file path of the CSV file
file_path = "marketing.csv"

# Call the function to analyze the CSV file
analyze_csv(file_path)
