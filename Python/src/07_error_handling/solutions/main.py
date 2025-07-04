import logging
from file_service import FileService, FileReader, FileWriter
import os

# Logging configuration
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("logger")

def main():
    try:
        file_reader = FileReader()
        file_writer = FileWriter()
        file_service = FileService()

        python_file = os.path.join(os.path.dirname(__file__), "main.py")
        content_file1 = file_reader.read_file(python_file) 
        print("======== Python file content ===========")
        print(content_file1)

        python_file_copy = "main.py.copy.txt"
        file_service.copy_file(python_file, python_file_copy)

        try:
            csv_content = os.path.join(os.path.dirname(__file__), "data.csv")
            print("======== CSV content ===========")
            for row in csv_content:
                print(row)
        except FileNotFoundError as ex:
            logger.error("Error while reading the CSV file", exc_info=True)

        content_file2 = file_reader.read_file("NonExisting")
        if content_file2 is None:
            print("File 'NonExisting' was not found")
        else:
            print(content_file2)

        # Demonstrating None value handling
        try:
            content_file3 = file_reader.read_file(None)
            print(content_file3)
        except ValueError as ex:
            logger.error(f"Invalid argument: {ex}", exc_info=True)

        print("File operations completed successfully")

    except FileNotFoundError as ex:
        logger.error("Error while reading the file", exc_info=True)
    except Exception as ex:
        logger.error("An unexpected error occurred", exc_info=True)

if __name__ == "__main__":
    main()