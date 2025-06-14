import os

from file_content import FileContent


class FileReader:
    def read_file(self, filename):
        if not os.path.exists(filename):
            return None
        file_content = FileContent(filename)
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        if lines:
            file_content.lines=lines
        return file_content

