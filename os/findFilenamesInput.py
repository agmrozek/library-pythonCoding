import os

def find_file(filename):
    for root, dirs, files in os.walk('/'): 
        if filename in files:
            print(f"Found file '{filename}' at: {os.path.join(root, filename)}")
            return  # exit the function if the file is found
    print(f"File '{filename}' not found on the system.") 

filename = input("Enter the filename to search for: ")
find_file(filename)

