
from pathlib import Path

def rename_files_to_numbers(folder_path, zero_pad=3):
    """
    Renames all files in the target directory to sequential numbers.
    Keeps the original file extensions.
    """
    path = Path(r"E:\Python\fast\image_crop.py\images")
    
    # Verify if the folder exists
    if not path.is_dir():
        print(f"Error: The directory '{r'E:\Python\fast\image_crop.py\images'}' does not exist.")
        return

    # Grab and sort all items that are files (ignores subdirectories)
    files = sorted([f for f in path.iterdir() if f.is_file()])
    
    if not files:
        print("No files found in the directory.")
        return

    print(f"Found {len(files)} files. Starting renaming process...\n")

    # Loop through sorted files with a 1-based index
    for index, file_path in enumerate(files, start=1):
        # Format the number with leading zeros (e.g., 001, 002)
        new_name = f"{str(index).zfill(zero_pad)}{file_path.suffix}"
        new_file_path = path / new_name
        
        try:
            file_path.rename(new_file_path)
            print(f"Renamed: '{new_file_path.name}' -> '{new_name}'")
        except Exception as e:
            print(f"Failed to rename '{file_path.name}': {e}")

    print("\nRenaming complete!")

# --- CONFIGURATION ---
# Replace this with the actual path to your folder
TARGET_FOLDER = r"C:\path\to\your\folder" 

# Run the function
rename_files_to_numbers(TARGET_FOLDER, zero_pad=3)
