import os
file_name="C:/Users/Sai Avinash/OneDrive/Desktop"
if os.path.exists(file_name):
    print(f"file exists '{file_name}'")

    if os.path.isfile(file_name):
        print("it is a file")
    if os.path.isdir(file_name):
        print("it is a directory")
else:
    print("file does not exist")


