# Data Cleaning Script

This Python script is designed to clean data in CSV or Excel files by:
- Removing duplicate rows
- Filling missing string values with "Unknown"
- Filling missing numeric values with the column mean
- Standardizing date columns to a consistent format

## Requirements

- Python 3.x
- `pandas` library (install via `pip install pandas`)

## How to Use

1. **Save the script**:
   Save the script as `main.py` on your local machine.

2. **Run the script**:
```bash
python main.py
```

3. **Input file path**:
   When prompted, provide the path to the data file (CSV or Excel) to clean.

4. **Check the cleaned data**:
   The script will save the cleaned data to a new file called `cleaned_data.csv`.

### Notes:
- The script expects date columns to contain the word "date" in their names (case-insensitive).
- Non-numeric columns will have missing values filled with "Unknown", and string columns will be converted to lowercase.
