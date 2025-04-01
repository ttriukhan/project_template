import pytest
from app.io.input import read_from_file_using_build_in, read_from_file_using_pandas
import os


def test_read_using_build_in_valid_file():
    """Checks if text read by method using build in functions from valid text file equals its content."""
    file_path = "../data/valid_text.txt"
    expected_text = "This is a valid test file."
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(expected_text)
    actual_text = read_from_file_using_build_in(file_path)
    assert actual_text == expected_text
    os.remove(file_path)


def test_read_using_build_in_empty_file():
    """Checks if text read by method using build in functions from empty text file equals ""."""
    file_path = "../data/empty_file.txt"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    open(file_path, "w").close()
    actual_text = read_from_file_using_build_in(file_path)
    assert actual_text == ""
    os.remove(file_path)


def test_read_using_build_in_non_existing_file():
    """Checks if method using build in functions raises FileNotFound error if file does not exist."""
    file_path = "../data/not_existing_file.txt"
    with pytest.raises(FileNotFoundError):
        read_from_file_using_build_in(file_path)
