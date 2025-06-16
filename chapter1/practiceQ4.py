import os

# Specify the directory path (or use '.' for the current directory)
directory_path = "."

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)

for item in contents:
    if os.path.isfile(os.path.join(directory_path, item)):
        print(f"File: {item}")
    else:
        print(f"Folder: {item}")