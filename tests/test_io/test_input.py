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


def test_read_valid_file_using_pandas():
    """Checks if text read by method using pandas from valid text file equals its content."""
    file_path = "../data/valid_data.csv"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    text_for_csv = """
        id,book_name,author
        1,Harry Potter,JK Rowling
        2,Colony,Max Kidruk
        3,Almost good guys,Daria Chaika
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text_for_csv)
    actual_data_frame = read_from_file_using_pandas(file_path)
    assert actual_data_frame.shape == (2, 2)
    assert actual_data_frame.iloc[1]["book_name"] == "Colony"
    os.remove(file_path)


def test_read_using_pandas_empty_file():
    """Checks if text read by method using build in functions from empty text file equals ""."""
    file_path = "../data/empty_file.csv"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    open(file_path, "w").close()
    actual_text = read_from_file_using_pandas(file_path)
    assert actual_text == ""
    os.remove(file_path)


def test_read_using_pandas_non_existing_file():
    """Checks if method using pandas raises FileNotFound error if file does not exist."""
    file_path = "../data/not_existing_file.csv"
    with pytest.raises(FileNotFoundError):
        read_from_file_using_build_in(file_path)
