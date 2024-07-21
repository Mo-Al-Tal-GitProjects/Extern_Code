# Step 1: Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def load_data(file_path):
    """
    Load dataset from an Excel file.

    Args:
    file_path (str): The path to the Excel file containing the dataset.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    df = pd.read_excel(file_path)
    print("Dataset loaded successfully.")
    print(df.head())
    print(df.info())
    return df

def calculate_frequencies(df):
    """
    Calculate the frequencies of True values for each boolean column.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    pd.Series: Frequencies of True values for each boolean column.
    """
    frequencies = df.select_dtypes(include='bool').sum()
    print("Frequencies calculated successfully.")
    print(frequencies)
    return frequencies

def visualize_frequencies(frequencies, title, xlabel, ylabel, figsize=(12, 6), rotation=45, fontsize=10):
    """
    Visualize the frequencies using a bar chart.

    Args:
    frequencies (pd.Series): The frequencies to visualize.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    figsize (tuple): The size of the figure.
    rotation (int): The rotation angle for x-axis labels.
    fontsize (int): The font size for labels and title.
    """
    sns.set_style("whitegrid")
    plt.figure(figsize=figsize)
    sns.barplot(x=frequencies.index, y=frequencies.values, palette='viridis')
    plt.title(title, fontsize=fontsize)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)
    plt.xticks(rotation=rotation, fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.show()

def main():
    # Prompt user for the file path
    file_path = input("Please enter the path to the Excel file: ")
    
    # Load the dataset
    df = load_data(file_path)
    
    # Calculate frequencies
    frequencies = calculate_frequencies(df)
    
    # Visualize frequencies
    visualize_frequencies(frequencies, 
                          title='Frequency of True Values for Each Risk Tag', 
                          xlabel='Risk Tags', 
                          ylabel='Frequency of True')

if __name__ == "__main__":
    main()
