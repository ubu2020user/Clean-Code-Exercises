import os
from typing import Optional

from file_content import FileContent


class FileReader:
    def read_file(self, filename) -> Optional[FileContent]:
        """
        Reads a file and returns its content.

        Args:
            filename: Path to the file to be read

        Returns:
            FileContent object or None if file doesn't exist

        Raises:
            ValueError: If filename is None
        """
        if filename is None:
            raise ValueError("Filename cannot be None")

        # Convert relative path to absolute path
        filename = os.path.abspath(filename)

        if not os.path.exists(filename):
            return None

        file_content = FileContent(filename)
        with open(filename, "r") as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines]
        if lines:
            file_content.lines = lines

        return file_content
