import app.io.input as inpt
import pandas
import pandas.testing as tm
import os


def test_read_valid_text_file():
    with open("test_file.txt", "w") as f:
        f.write("Hello, World!")
    expected = "Hello, World!"

    actual = inpt.read_file_with_python("test_file.txt")
    os.remove("test_file.txt")

    assert expected == actual


def test_read_nonexistent_file():
    expected = None

    actual = inpt.read_file_with_python("nonexistent_file.txt")

    assert expected == actual


def test_read_empty_file():
    with open("test_file.txt", "w") as f:
        f.write("")
    expected = ""

    result = inpt.read_file_with_python("test_file.txt")
    os.remove("test_file.txt")

    assert expected == result


def test_read_valid_csv_file():
    data = pandas.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    data.to_csv("test_file.csv", index=False)
    expected = pandas.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})

    actual = inpt.read_file_with_pandas("test_file.csv", "csv")
    os.remove("test_file.csv")

    tm.assert_frame_equal(actual, expected)


def test_read_valid_json_file():
    data = pandas.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    data.to_json("test_file.json", orient="records")
    expected = pandas.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})

    actual = inpt.read_file_with_pandas("test_file.json", "json")
    os.remove("test_file.json")

    tm.assert_frame_equal(actual, expected)


def test_read_unsupported_file_type():
    with open("test_file.txt", "w") as f:
        f.write("Hello, World!")

    expected = None

    actual = inpt.read_file_with_pandas("test_file.txt", "txt")
    os.remove("test_file.txt")

    assert actual == expected
