import sys

def process_files(input_file, output_file):
    try:
        if not input_file or not output_file:
            raise ValueError("Both input and output file paths must be provided.")

        with open(input_file, 'r') as inp:
            content = inp.read()

        processed_content = content.upper()  
        with open(output_file, 'w') as output:
            output.write(processed_content)

        print("File processing completed successfully.")

    except FileNotFoundError:
        print("Input file not found.")
        sys.exit(1)
    except PermissionError:
        print("Permission denied while writing to the output file.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_program.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_files(input_file, output_file)
