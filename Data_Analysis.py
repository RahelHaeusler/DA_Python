#inspiraton https://www.kaggle.com/code/janiobachmann/bank-marketing-campaign-opening-a-term-deposit/notebook

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_csv(file_path):
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

    #show number of occurence per each unique value
    print(df['marital'].value_counts())
    print(df['default'].value_counts())
    print(df['housing'].value_counts())
    print(df['loan'].value_counts())
    print(df['month'].value_counts())
    print(df['day_of_week'].value_counts())
    print(df['campaign'].value_counts())
    print(df['previous'].value_counts())
    print(df['poutcome'].value_counts())

    #Histogram for age
    plt.figure(figsize=(8, 6))
    plt.hist(df['age'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    #Histogram for month
    plt.figure(figsize=(8, 6))
    plt.hist(df['month'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Month Distribution')
    plt.xlabel('Month')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    #Histogram for day of week
    plt.figure(figsize=(8, 6))
    plt.hist(df['day_of_week'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Day of Week Distribution')
    plt.xlabel('Day of Week')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    #Histogram for campaign
    plt.figure(figsize=(8, 6))
    plt.hist(df['campaign'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Campaign Distribution')
    plt.xlabel('Campaign')
    plt.ylabel('Number')
    plt.grid(True)
    plt.show()


def visualize_csv(file_path):
    # Finding the unique values of y
    df['y'].unique()
    print(df['y'].unique())
    # how many people(client) have subscribed to a term deposit?
    df.y.value_counts()
    print(df.y.value_counts())
    sns.set(font_scale=1.5)
    countplt = sns.countplot(x='y', data=df, palette='Set1')
    plt.show()

    plt.style.use('ggplot')

    df.hist(bins=20, figsize=(14, 10), color='#E14906')
    plt.show()

def scatterplot(df):
    # Scatter Plot for age and subscription to fixed term deposit
    plt.figure(figsize=(8, 6))
    plt.scatter(df['age'], df['y'], color='blue', alpha=0.5)
    plt.title('Scatterplot of Age and Y')
    plt.xlabel('Age')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# Provide the file path of the CSV file
file_path = "marketing.csv"
# Read the CSV file into a pandas DataFrame with semicolon as delimiter
df = pd.read_csv(file_path, delimiter=';')
# Call the function to analyze the CSV file
analyze_csv(file_path)
#visualize_csv(file_path)
#Scatterplot variables towards the Subscription (Y) does not make sense, as there are only two variables
#for each subscription
#scatterplot(df)

