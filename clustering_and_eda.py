import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
import scipy.cluster.hierarchy as sch

def subset_data(df, n, top_n=True):
    frequencies = df.select_dtypes(include='bool').sum()
    if top_n:
        top_n_features = frequencies.nlargest(n).index.tolist()
    else:
        top_n_features = frequencies.nsmallest(n).index.tolist()
    return df[top_n_features]

def calculate_distance_matrix(df):
    binary_df = df.replace({True: 1, False: 0})
    distance_matrix = pdist(binary_df, 'jaccard')
    return squareform(distance_matrix)

def hierarchical_clustering(distance_matrix, title, figsize=(12, 8)):
    linkage_matrix = sch.linkage(distance_matrix, method='ward')
    plt.figure(figsize=figsize)
    dendrogram = sch.dendrogram(linkage_matrix)
    plt.title(title)
    plt.xlabel('Sample index = Smart Contract')
    plt.ylabel('Distance')
    plt.show()

def main():
    from data_loading_and_processing import load_data
    file_path = input("Please enter the path to the Excel file: ")
    n = int(input("Please enter the number of features to subset: "))
    top_n_choice = input("Do you want to use the top N features? (yes/no): ").strip().lower() == 'yes'
    max_rows = int(input("Please enter the maximum number of rows to include (e.g., 200): "))
    
    df = load_data(file_path)
    df_subset = subset_data(df, n, top_n_choice)
    
    # Subset rows if necessary
    if df_subset.shape[0] > max_rows:
        df_subset = df_subset.sample(n=max_rows, random_state=42)
    
    distance_matrix = calculate_distance_matrix(df_subset)
    hierarchical_clustering(distance_matrix, title='Hierarchical Clustering Dendrogram', figsize=(12, 8))

if __name__ == "__main__":
    main()
