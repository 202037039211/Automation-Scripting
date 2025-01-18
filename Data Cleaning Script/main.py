import pandas as pd

def clean_data(file_path):
    """
    Function to clean data from a given file (CSV or Excel).
    - Removes duplicates
    - Fills missing values for strings and numbers
    - Standardizes date columns
    - Saves cleaned data to 'cleaned_data.csv'
    """

    # Load data from the provided file
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        print("Unsupported file format. Please provide a .csv or .xlsx file.")
        return

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Handle missing values and standardize data formats
    for col in df.columns:
        if df[col].dtype == "object":
            # Fill missing string values with "Unknown" and convert text to lowercase
            df[col] = df[col].fillna("Unknown").apply(lambda x: x.lower() if isinstance(x, str) else x)
        elif df[col].dtype in ["int64", "float64"]:
            # Fill missing numeric values with the column's mean
            df[col] = df[col].fillna(df[col].mean())
    
    # Standardize date columns by converting them to datetime format
    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True)
            except ValueError:
                pass  # Ignore columns that can't be converted to date

    # Save the cleaned data to a new CSV file
    df.to_csv("cleaned_data.csv", index=False)
    print("Cleaned data saved to cleaned_data.csv")

def main():
    """
    Main function to prompt user for file path and initiate data cleaning.
    """
    file_path = input("Enter the path of the data file to clean (.csv or .xlsx): ")
    clean_data(file_path)

if __name__ == "__main__":
    main()
