import json
student_details={
    "name":"vinay",
    "regno":49,
    "skill":"python"
}
file_path="C:/Users/Sai Avinash/OneDrive/Desktop/python/file.json"
try:
    with open(file_path,"w") as file:
        json.dump(student_details,file,indent=4)
        print(f"json file has been created  {file_path}")
except FileExistsError:
    print("the file already exists")

