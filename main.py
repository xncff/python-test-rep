import app.io.input as inpt
import app.io.output as otpt


def main():
    console_input = inpt.input_text()
    print(console_input, '\n')

    text_file_content = inpt.read_file_with_python("text_to_read.txt")
    print(text_file_content, '\n')

    csv_data = inpt.read_file_with_pandas("csv_to_read.csv", "csv")
    print(csv_data, '\n')

    combined = console_input + '\n' + text_file_content + '\n' + csv_data.to_string()

    output_file = "result.txt"
    otpt.write_to_file_with_python(combined, output_file)


if __name__ == "__main__":
    main()
