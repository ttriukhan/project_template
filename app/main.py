from app.io.input import read_from_console, read_from_file_using_build_in, read_from_file_using_pandas
from app.io.output import write_to_console, write_to_file_using_build_in
import os

def main():
    data_folder = "..\data"
    input_txt_file_path = os.path.join(data_folder, "input.txt")
    input_csv_file_path = os.path.join(data_folder, "input.csv")
    output_file_path = os.path.join(data_folder, "output.txt")

    text_console = read_from_console()
    text_file = read_from_file_using_build_in(input_txt_file_path)
    text_pandas = read_from_file_using_pandas(input_csv_file_path)
    text_for_output = "\n\n".join([
        f"Console Input:\n{text_console}",
        f"File Content:\n{text_file}",
        f"CSV Content:\n{text_pandas}"
    ])

    write_to_console(text_for_output)
    write_to_file_using_build_in(output_file_path, text_for_output)


if __name__ == "__main__":
    main()
