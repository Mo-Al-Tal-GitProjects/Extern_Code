# Step 4: Import necessary libraries (if not already imported)
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

def find_top_n_related_pairs(phi_matrix, n=10):
    """
    Find the top N closely related risk tag pairs based on Phi coefficient.

    Args:
    phi_matrix (pd.DataFrame): DataFrame containing Phi coefficients.
    n (int): Number of top related pairs to return.

    Returns:
    pd.DataFrame: DataFrame with top N related risk tag pairs.
    """
    phi_matrix_unstacked = phi_matrix.unstack().reset_index()
    phi_matrix_unstacked.columns = ['Risk_Tag_1', 'Risk_Tag_2', 'Phi_Coefficient']
    phi_matrix_unstacked = phi_matrix_unstacked[phi_matrix_unstacked['Risk_Tag_1'] != phi_matrix_unstacked['Risk_Tag_2']]
    top_n_related_pairs = phi_matrix_unstacked.sort_values(by='Phi_Coefficient', ascending=False).head(n)
    return top_n_related_pairs

def visualize_related_pairs(pairs_df, title, xlabel, ylabel, figsize=(12, 6), rotation=45, fontsize=10):
    """
    Visualize the related risk tag pairs using a bar chart.

    Args:
    pairs_df (pd.DataFrame): DataFrame containing related pairs and their Phi coefficients.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    figsize (tuple): The size of the figure.
    rotation (int): The rotation angle for x-axis labels.
    fontsize (int): The font size for labels and title.
    """
    sns.set_style("whitegrid")
    plt.figure(figsize=figsize)
    sns.barplot(x='Phi_Coefficient', y=pairs_df[['Risk_Tag_1', 'Risk_Tag_2']].apply(lambda x: f"{x[0]} & {x[1]}", axis=1), data=pairs_df, palette='viridis')
    plt.title(title, fontsize=fontsize)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)
    plt.xticks(rotation=rotation, fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.show()

def main():
    # Prompt user for the file path and number of top related pairs
    file_path = input("Please enter the path to the Excel file: ")
    n = int(input("Please enter the number of top related pairs to display: "))
    
    # Load the dataset
    df = pd.read_excel(file_path)
    
    # Calculate Phi coefficients
    phi_matrix = calculate_phi_matrix(df)
    
    # Find top N related pairs
    top_n_related_pairs = find_top_n_related_pairs(phi_matrix, n=n)
    
    # Visualize related pairs
    visualize_related_pairs(top_n_related_pairs, 
                            title=f'Top {n} Closely Related Risk Pairs', 
                            xlabel='Phi Coefficient', 
                            ylabel='Risk Tag Pairs')

if __name__ == "__main__":
    main()
