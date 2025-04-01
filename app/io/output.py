import pandas


def print_text(text):
    """Prints text to the console.

    Args:
        text (str): Text to print.

    """
    print(text)


def write_to_file_with_python(text, file_path):
    """Writes text to a file using Python's standard file operations.

    Args:
        text (str): The text to be written to the file.
        file_path (str): Path of the file to be written to.

    """
    try:
        with open(file_path, 'w') as f:
            f.write(text)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")


def write_to_file_with_pandas(data, file_path, file_type="csv"):
    """Writes to a file based on its type using pandas package.

    Args:
        data: Any pandas-supported type. Data to be written to the file.
        file_path (str): Path of the file to be written to.
        file_type (str): Type of the file.

    """
    try:
        if file_type == "csv":
            data.to_csv(file_path)
        elif file_type == "json":
            data.to_json(file_path)
        else:
            print(f"Error: Unsupported file type: {file_type}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
