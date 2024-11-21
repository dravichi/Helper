"""
No external library is needed, the program can be run immediately
"""

import os

def rename_files(file_folder, formats_to_rename, base_name, start_index):
    # List all files in the specified folder
    files = os.listdir(file_folder)
    
    # Filter out only files that match the specified formats
    files_to_rename = [file for file in files if any(file.lower().endswith(fmt) for fmt in formats_to_rename)]
    
    # Sort the files to ensure consistent renaming
    files_to_rename.sort()
    
    # Rename files in the folder
    for i, file in enumerate(files_to_rename, start=start_index):
        # Construct the new filename
        # Get the original file extension (e.g., .txt, .mp4, .png)
        file_extension = os.path.splitext(file)[1]
        
        # Format the new name as "base_name_n" (e.g., report_1.txt, photo_2.png)
        new_name = f"{base_name}_{i}{file_extension}"
        
        # Create the full file path for both old and new names
        old_path = os.path.join(file_folder, file)
        new_path = os.path.join(file_folder, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed '{file}' to '{new_name}'")

if __name__ == "__main__":
    # User-defined folder path
    file_folder = input("Enter the path of the folder containing files: ")
    # User-defined formats
    formats_input = input("Enter the file formats to rename (comma-separated, e.g., '.txt, .jpg'): ") 
    # Convert the input into a list of formats
    formats_to_rename = [fmt.strip() for fmt in formats_input.split(',')] 
    # User-defined base name (e.g., "document")
    base_name = input("Enter the base name for the new files (e.g., 'document'): ")
    # User-defined starting index
    start_index = int(input("Enter the starting index for renaming (e.g., 1): "))
    
    # Call the rename_files function
    rename_files(file_folder, formats_to_rename, base_name, start_index)
