import os

def search_file(directory, filename):
    try:
        for root, dirs, files in os.walk(directory):
            if filename in files:
                return os.path.join(root, filename)
        return "File not found"
    except Exception as e:
        return f"Error: {e}"

directory = os.getcwd()
filename = input("Enter the filename")
result = search_file(directory, filename)
print(result)
