from file_reader import FileReader
from file_writer import FileWriter


class FileService:
    def __init__(self):
        self.file_reader = FileReader()
        self.file_writer = FileWriter()

    def copy_file(self, filename_source, filename_destination):
        # Read file
        content = self.file_reader.read_file(filename_source)
        if content is None:
            raise FileNotFoundError(f"The source file {filename_source} was not found.")

        # Set the filename for the destination
        content.name = filename_destination

        # Write file
        self.file_writer.write_file(content, overwrite=True, append_content_to_file=True)

    def read_csv(self, filename):
        # Read CSV file
        file_content = self.file_reader.read_file(filename)
        if file_content is None or file_content.lines is None:
            raise FileNotFoundError(f"The file {filename} was not found or contains no lines.")

        # Process each line into a list of cells
        list_of_values = [line.split(',') for line in file_content.lines]

        # Remove whitespace in each cell
        list_of_values = [[cell.strip() for cell in row] for row in list_of_values]

        return list_of_values
