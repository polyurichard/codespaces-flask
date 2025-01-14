import json

# Read the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Process the JSON data
students = data['students']

for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print("Grades:")
    for subject, grade in student['grades'].items():
        print(f"  {subject}: {grade}")
    print()