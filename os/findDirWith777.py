import os

def find_directories_with_777_permissions(top_dir):
    directories = []
    for dirpath, dirnames, filenames in os.walk(top_dir):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            mode = os.stat(full_path).st_mode
            if (mode & 0o777) == 0o777:
                directories.append(full_path)
    return directories

top_dir = input("Enter the top-level directory to search: ")

directories = find_directories_with_777_permissions(top_dir)
print("Directories with 777 permissions:")
for directory in directories:
    print(directory)

