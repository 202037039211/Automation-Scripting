import os
import shutil
from datetime import datetime

def rename_and_organize_files(directory, category):
    """
    Renames and organizes files in the specified directory based on their modification date and category.

    Args:
    - directory (str): Path to the directory containing files to organize
    - category (str): Category name to organize the files into respective subfolders
    """
    directory = os.path.expanduser(directory)  # Expand '~' to full home directory path
    
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(('.txt', '.jpg', '.png', '.pdf')):  # Filter by file types
            file_path = os.path.join(directory, filename)
            modification_time = os.path.getmtime(file_path)  # Get file modification time
            date_str = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d')
            
            # Define the new filename and category folder path
            new_filename = f"{category}_{date_str}_{filename}"
            category_folder = os.path.join(directory, category)

            # Create the category folder if it doesn't exist
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            # Move and rename the file to the new location
            new_file_path = os.path.join(category_folder, new_filename)
            shutil.move(file_path, new_file_path)
            print(f"Moved: {filename} -> {new_filename}")

def main():
    """
    Main function to get input from the user and execute the file renaming and organizing process.
    """
    directory = input("Enter the directory path to organize files: ")
    category = input("Enter the category name for organizing files: ")
    rename_and_organize_files(directory, category)
    print("File organization complete.")

if __name__ == "__main__":
    main()
