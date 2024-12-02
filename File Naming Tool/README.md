# File Naming Tool

This Python tool helps you organize files in a directory by renaming them based on their modification date and categorizing them into separate folders.

## Features

- **Rename Files**: Files are renamed with a prefix containing the category and modification date (e.g., `Work_2024-12-01_filename.txt`).
- **Organize Files**: Files are moved into a subfolder named after the specified category.

## Requirements

- Python 3.x
- `os`, `shutil`, and `datetime` (all are included in Python's standard library)

## Installation

1. Clone or download this repository.
2. Place the script in the directory containing the files you wish to organize.
3. Run the script in your terminal or Python IDE.

## Usage

1. Run the script.
2. When prompted, enter the directory path where your files are located.
3. Enter the category name to organize the files (e.g., `Work`, `Personal`).
4. The files will be renamed with the category and modification date, and moved into the corresponding folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
