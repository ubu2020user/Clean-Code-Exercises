import os

class FileWriter:
    def write_file(self, file_content, overwrite=False, append_content_to_file=False):
        filename = file_content.name
        file_exists = os.path.exists(filename)

        if not overwrite and file_exists:
            raise IOError("File exists")

        mode = 'w'  # Default mode is writing, overwrites the file
        if append_content_to_file and file_exists:
            mode = 'a'  # Change the mode to append if append_content_to_file is True

        with open(filename, mode, encoding='utf-8') as file:
            if file_content.lines:
                file.write('\n'.join(file_content.lines))
