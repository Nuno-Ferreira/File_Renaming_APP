"""Test the rename files script."""

from pathlib import Path
from src.script import rename_files


def test_rename_files(tmp_path: Path) -> None:
    """Test the rename files script."""

    # Create the files
    tmp_path.joinpath("file1.txt").touch()
    tmp_path.joinpath("file2.txt").touch()
    tmp_path.joinpath("file3.txt").touch()

    # Set the new name
    new_name = "new_file"

    # Rename the files
    rename_files(directory=tmp_path, new_name=new_name)

    # Check the files have been renamed
    assert tmp_path.joinpath("new_file_0.txt").exists()
    assert tmp_path.joinpath("new_file_1.txt").exists()
    assert tmp_path.joinpath("new_file_2.txt").exists()
