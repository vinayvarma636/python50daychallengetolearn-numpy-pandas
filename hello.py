import json
import csv
student_details=[["name","age","rollno"
"teju",20,30,
"vinay",20,49]]
file_path="C:/Users/Sai Avinash/OneDrive/Desktop/python/c.csv"
try:
    with open(file_path,"w") as file:
        writer=csv.writer(file)
        for details in student_details:
            writer.writerow(details) 
        print(f"csv file has been created  {file_path}")
except FileExistsError:
    print("the file already exists")