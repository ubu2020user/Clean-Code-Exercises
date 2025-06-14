import logging
from file_service import FileService, FileReader, FileWriter

# Logging configuration
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("logger")

def main():
    try:
        file_reader = FileReader()
        file_writer = FileWriter()
        file_service = FileService()

        python_file = "main.py"
        content_file1 = file_reader.read_file(python_file) 
        print("======== Python file content ===========")
        print(content_file1)

        python_file_copy = "main.py.copy.txt"
        file_service.copy_file(python_file, python_file_copy)

        try:
            csv_content = file_service.read_csv("./data.csv")
            if not csv_content:
                raise FileNotFoundError("The file './data.csv' was found but contains no lines.")
            print("======== CSV content ===========")
            for row in csv_content:
                print(row)
        except FileNotFoundError as ex:
            logger.error("Error while reading the CSV file", exc_info=True)

        content_file2 = file_reader.read_file("NonExisting")
        print(content_file2)

        # Failing operations:
        content_file3 = file_reader.read_file(None)
        print(content_file3)

    except FileNotFoundError as ex:
        logger.error("Error while reading the file", exc_info=True)
    except Exception as ex:
        logger.error("An unexpected error occurred", exc_info=True)

if __name__ == "__main__":
    main()
