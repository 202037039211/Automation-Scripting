import pandas as pd

# Function to analyze data from a CSV or Excel file
def analyze_data(file_path):
    # Load the data based on file extension
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        print("Unsupported file format. Please provide a .csv or .xlsx file.")
        return

    # Display the first few rows of the DataFrame to ensure it's loaded correctly
    print("Data loaded successfully. Here are the first few rows:")
    print(df.head())

    # Initialize a dictionary to store summary statistics
    summary_data = {
        'Metrics': [],
        'Counts': [],
        'Mean': [],
        'Median': [],
        'Std Dev': [],
        'Sum': []
    }

    # Count unique values for categorical columns (object data type)
    for column in df.select_dtypes(include=['object']).columns:
        summary_data['Metrics'].append(column)
        summary_data['Counts'].append(df[column].nunique())  # Count unique values
        summary_data['Mean'].append(None)
        summary_data['Median'].append(None)
        summary_data['Std Dev'].append(None)
        summary_data['Sum'].append(None)

    # Calculate mean, median, std dev, and sum for numerical columns
    for column in df.select_dtypes(include=['number']).columns:
        summary_data['Metrics'].append(column)
        summary_data['Counts'].append(None)
        summary_data['Mean'].append(df[column].mean())   # Mean of the column
        summary_data['Median'].append(df[column].median())  # Median of the column
        summary_data['Std Dev'].append(df[column].std())   # Standard deviation
        summary_data['Sum'].append(df[column].sum())   # Sum of the column

    # Create a DataFrame for the summary statistics
    summary_df = pd.DataFrame(summary_data)

    # Save the summary data to a CSV file for further use
    summary_df.to_csv('data_summary.csv', index=False)
    print("Summary data saved to data_summary.csv")

# Main function to run the analysis
def main():
    file_path = input("Enter the path of the data file (.csv or .xlsx) to analyze: ")
    analyze_data(file_path)

# Ensure the script is executed directly (not imported)
if __name__ == "__main__":
    main()
