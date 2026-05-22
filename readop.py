# reading a file
import json
student_details={
    "name":"vinay",
    "regno":49,
    "skill":"python"
}
file_path="C:/Users/Sai Avinash/OneDrive/Desktop/python/file.json"
try:
    with open(file_path,"r") as file:
        content=json.load(file)
        print(content["name"])
except FileExistsError:
    print("the file already exists")

