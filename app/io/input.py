import pandas


def read_from_console():
    """
    This function reads input from console.

    Returns:
        (str): text read from console.
    """
    return input("Enter text: ")


def read_from_file_using_build_in(file_path):
    """
    This function reads from file using build in Python functions.

    Args:
        file_path (str): path to file for reading.

    Returns:
        (str): text read from file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_from_file_using_pandas(file_path):
    """
    This function reads from file using Pandas.

    Args:
        file_path (str): path to file for reading.

    Returns:
        (str): text read from file.
    """
    try:
        file_content = pandas.read_csv(file_path)
        return file_content.to_string()
    except pandas.errors.EmptyDataError:
        return ""
