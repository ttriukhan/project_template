import pandas
import os

def write_to_console(text):
    """
    This function writes text to console.

    Args:
        text (str): Text to be written.

    Returns:
        None
    """
    print(text)


def write_to_file_using_build_in(file_path, text):
    """
    This function writes text to file using build in Python functions.
    If file does not exist, it creates it.

    Args:
        file_path (str): path to file for reading.
        text (str): text to be written.

    Returns:
        None
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
