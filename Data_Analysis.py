# inspiraton https://www.kaggle.com/code/janiobachmann/bank-marketing-campaign-opening-a-term-deposit/notebook
# see possible data visualization
# https://medium.com/@caglarlaledemir/data-visualization-with-python-seaborn-library-3d276302d715

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# functions to analyze the dataset
################################

def statistics_csv(df):
    # Display basic statistics of numerical columns
    print("\nBasic statistics of numerical columns:")
    print(df.describe())
    summary = df.describe()
    table_html = summary.to_html()
    # Write the HTML table to a file
    with open('summary_table.html', 'w') as f:
        f.write(table_html)

# functions for getting a feeling of the variables


def analyze_csv(df):
    # Display the first few rows of the DataFrame
    print("First few rows of the data:")
    print(df.head())

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

    # show number of occurence per each unique value
    print(df['marital'].value_counts())
    print(df['default'].value_counts())
    print(df['housing'].value_counts())
    print(df['loan'].value_counts())
    print(df['month'].value_counts())
    print(df['day_of_week'].value_counts())
    print(df['campaign'].value_counts())
    print(df['previous'].value_counts())
    print(df['poutcome'].value_counts())


def visualize_csv(df):
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


#def scatterplot(df):
    # Scatter Plot for age and subscription to fixed term deposit
    plt.figure(figsize=(8, 6))
    plt.scatter(df['age'], df['y'], color='blue', alpha=0.5)
    plt.title('Scatterplot of Age and Y')
    plt.xlabel('Age')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


def histogramplot(df):
    # Histogram for age
    plt.figure(figsize=(8, 6))
    plt.hist(df['age'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Histogram for month
    plt.figure(figsize=(8, 6))
    plt.hist(df['month'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Month Distribution')
    plt.xlabel('Month')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Histogram for day of week
    plt.figure(figsize=(8, 6))
    plt.hist(df['day_of_week'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Day of Week Distribution')
    plt.xlabel('Day of Week')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Histogram for campaign
    plt.figure(figsize=(8, 6))
    plt.hist(df['campaign'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Campaign Distribution')
    plt.xlabel('Campaign')
    plt.ylabel('Number')
    plt.grid(True)
    plt.show()

def check_duplicates(df):
    # Check for duplicate rows
    duplicates = df.duplicated()

    # Count the number of duplicate rows
    num_duplicates = duplicates.sum()

    if num_duplicates > 0:
        print("Duplicate rows found:")
        print(df[duplicates])
    else:
        print("No duplicate rows found.")

def boxplot(df):
    # Plotting
    plt.figure(figsize=(8, 6))
    plt.boxplot(df['previous'])
    plt.title('Box Plot of Previous')
    plt.xlabel('Variable')
    plt.ylabel('Values')
    plt.grid(True)
    plt.show()

def histogram(df):
    # Filter out non-numeric columns
    numeric_columns = df.select_dtypes(include=['int', 'float']).columns

    # Create histograms for each numeric variable
    for column in numeric_columns:
        plt.figure(figsize=(8, 6))
        plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

def scatterplot(df):
    # Replace missing values with a placeholder (e.g., NaN)
    df.fillna(value=np.nan, inplace=True)

    # Create a pairplot
    sns.pairplot(df)
    plt.show()

def boxplot(df):
    numerical_columns = ['age', 'campaign', 'previous', 'emp.var.rate',
                         'cons.price.idx', 'cons.conf.idx', 'euribor3m']  # Add other numerical variables

    for column in numerical_columns:
        plt.figure(figsize=(8, 6))
        plt.boxplot(df[column])
        plt.title(f'Box Plot of {column}')
        plt.ylabel(column)
        plt.grid(True)
        plt.show()

def heatmap(df):
    # Select numeric columns (excluding 'y' if it's the target variable)
    numeric_columns = ['age', 'campaign', 'previous', 'emp.var.rate',
                       'cons.price.idx', 'cons.conf.idx', 'euribor3m']

    # Calculate the correlation matrix
    corr_matrix = df[numeric_columns].corr()

    # Plot the heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.show()

def pairplot(df):
    # Load the dataset into a DataFrame
    df = pd.read_csv('your_dataset.csv')

    # If 'y' is the target variable, drop it from the DataFrame
    if 'y' in df.columns:
        df.drop(columns=['y'], inplace=True)

    # Encode categorical variables if needed
    # For example, if 'job' is a categorical variable:
    # df['job'] = df['job'].astype('category').cat.codes

    # Create pairplot
    sns.pairplot(df)
    plt.show()

# Provide the file path of the CSV file
file_path = "marketing.csv"
# Read the CSV file into a pandas DataFrame with semicolon as delimiter
df = pd.read_csv(file_path, delimiter=';')
# Call the function to analyze the CSV file
# uncomment the line to run the function
# statistics_csv(df)
# analyze_csv(df)
# visualize_csv(df)
# histogramplot(df)
# check_duplicates(df)
# boxplot(df)
# histogram(df)
# scatterplot(df)
# boxplot(df)
# heatmap(df)
# pairplot not running yet
# pairplot(df)