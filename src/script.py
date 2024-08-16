"""Logic to rename the files in the directory."""

from pathlib import Path

def rename_files(directory: str, new_name: str) -> None:
    """Rename the files in the directory."""

    # Get the directory path
    directory_path = Path(directory)

    # Get the files in the directory
    files = list(directory_path.glob("*"))

    # Loop through the files and rename them
    for index, file in enumerate(files):
        # Ensure it is a file and not a directory
        if file.is_file():
            # Extract the file extension
            file_extension = file.suffix

            # Create the new file name with the extension
            new_file_name = directory_path / f"{new_name}_{index}{file_extension}"

            # Rename the file
            file.rename(new_file_name)
