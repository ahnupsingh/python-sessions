# Problem: Write a Python program to implement a file search tool that searches for a specific file name in a directory and its subdirectories.

import os

def search_file_recursive(directory, target_file):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            result = search_file_recursive(item_path, target_file)
            if result:
                return result
        elif item == target_file:
            return item_path
    return None

# Example usage:
start_directory = './'
file_to_find = 'recursive_directory_search.py'

result = search_file_recursive(start_directory, file_to_find)
if result:
    print("File found at:", result)
else:
    print("File not found in the directory.")