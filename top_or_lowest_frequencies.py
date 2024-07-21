# Step 3: Import necessary libraries (if not already imported)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def find_top_or_lowest_n_frequencies(frequencies, n=10, highest=True):
    """
    Find the top or lowest N frequency counts.

    Args:
    frequencies (pd.Series): Frequencies of True values for each boolean column.
    n (int): Number of top or lowest frequencies to return.
    highest (bool): Whether to return the highest frequencies. If False, returns the lowest frequencies.

    Returns:
    pd.Series: The top or lowest N frequency counts.
    """
    if highest:
        return frequencies.nlargest(n)
    else:
        return frequencies.nsmallest(n)

def visualize_top_or_lowest_n_frequencies(frequencies, title, xlabel, ylabel, figsize=(12, 6), rotation=45, fontsize=10):
    """
    Visualize the top or lowest N frequencies using a bar chart.

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
    # Prompt user for the file path, number of frequencies, and choice between top or lowest
    file_path = input("Please enter the path to the Excel file: ")
    n = int(input("Please enter the number of frequencies to display: "))
    choice = input("Do you want to display the top or lowest frequencies? (top/lowest): ").strip().lower()
    highest = True if choice == 'top' else False
    
    # Load the dataset
    df = pd.read_excel(file_path)
    
    # Calculate frequencies
    frequencies = df.select_dtypes(include='bool').sum()
    
    # Find top or lowest N frequencies
    top_or_lowest_n_frequencies = find_top_or_lowest_n_frequencies(frequencies, n=n, highest=highest)
    
    # Visualize top or lowest N frequencies
    title = 'Top {} {} Frequency Counts of True'.format(n, 'Highest' if highest else 'Lowest')
    visualize_top_or_lowest_n_frequencies(top_or_lowest_n_frequencies, title=title, xlabel='Risk Tags', ylabel='Frequency of True')

if __name__ == "__main__":
    main()
