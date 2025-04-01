import pandas


def input_text():
    """Reads input from the console.

    Returns:
        str: The input provided by the user.

   """
    user_input = input("Enter: ")
    return user_input


def read_file_with_python(file_path):
    """Reads a file using Python's standard file operations.

    Args:
        file_path (str): Path of the file to be read.

    Returns:
        str: Contents of the file.

    """
    try:
        with open(file_path, 'r') as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def read_file_with_pandas(file_path, file_type="csv"):
    """Reads a file based on its type using pandas package.

    Args:
        file_path (str): Path of the file to be read.
        file_type (str): Type of the file.

    Returns:
        pandas.DataFrame: Contents of the file.

    """
    try:
        if file_type == "csv":
            data = pandas.read_csv(file_path)
        elif file_type == "json":
            data = pandas.read_json(file_path)
        else:
            print(f"Error: Unsupported file type: {file_type}")
            return None
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

