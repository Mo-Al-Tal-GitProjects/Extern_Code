# Step 2: Import necessary libraries (if not already imported)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def phi_coefficient(x, y):
    """
    Calculate the Phi coefficient for two binary variables.

    Args:
    x (pd.Series): First binary variable.
    y (pd.Series): Second binary variable.

    Returns:
    float: Phi coefficient value.
    """
    contingency_table = pd.crosstab(x, y)
    chi2 = scipy.stats.chi2_contingency(contingency_table, correction=False)[0]
    n = np.sum(np.sum(contingency_table))
    phi = np.sqrt(chi2 / n)
    return phi

def calculate_phi_matrix(df):
    """
    Calculate the Phi coefficients for all pairs of boolean columns.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    pd.DataFrame: A DataFrame with Phi coefficients.
    """
    binary_variables = df.columns[df.dtypes == 'bool']
    phi_matrix = pd.DataFrame(index=binary_variables, columns=binary_variables)
    
    for var1 in binary_variables:
        for var2 in binary_variables:
            phi_matrix.loc[var1, var2] = phi_coefficient(df[var1], df[var2])
    
    print("Phi coefficients calculated for all pairs of variables.")
    return phi_matrix

def visualize_phi_matrix(phi_matrix, title, figsize=(12, 10)):
    """
    Visualize the Phi coefficients using a heatmap.

    Args:
    phi_matrix (pd.DataFrame): DataFrame containing Phi coefficients.
    title (str): Title of the heatmap.
    figsize (tuple): Size of the heatmap figure.
    """
    plt.figure(figsize=figsize)
    sns.heatmap(phi_matrix.astype(float), annot=False, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(title)
    plt.show()

def main():
    # Prompt user for the file path
    file_path = input("Please enter the path to the Excel file: ")
    
    # Load the dataset
    df = pd.read_excel(file_path)
    
    # Calculate Phi coefficients
    phi_matrix = calculate_phi_matrix(df)
    
    # Visualize Phi matrix
    visualize_phi_matrix(phi_matrix, title='Heatmap of Phi Coefficients Between Risk Tags')

if __name__ == "__main__":
    main()
