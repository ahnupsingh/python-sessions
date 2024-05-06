import os


def search_file(directory, filename):

    if not os.path.exists(directory):
        raise ValueError("Provided directory does not exist: " + directory)
    if not os.path.isdir(directory):
        raise ValueError("Provided path is not a directory: " + directory)

    try:
        # List contents of the current directory
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isdir(full_path):
                # If the entry is a directory, call the recursive function
                result = search_file(full_path, filename)
                if result != "File not found":
                    return result
            elif entry == filename:
                return full_path
    except PermissionError as e:
        # Permission error handling
        raise PermissionError("Permission denied: " + str(e))

    return "File not found"


try:
    print(search_file("D:\python-sessions", "file.py"))
except Exception as e:
    print(e)
