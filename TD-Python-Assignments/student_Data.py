# Dictionary to store student names and grades
students = {
    "Rahul": "A",
    "Neha": "B",
    "Sandeep": "D"
}

# --- Add a new student and grade ---
name = input("Enter new student name: ")
grade = input("Enter grade: ")

# If the name is not already present
if name not in students:  
    students[name] = grade
    print(f"{name} added with grade {grade}.")
else:
    print(f"{name} already exists.")

# --- Update an existing student's grade ---
name = input("Enter the student name to update: ")

# If the name exists
if name in students:  
    grade = input("Enter new grade: ")
    students[name] = grade
    print(f"{name}'s grade updated to: {grade}")
else:
    print(f"{name} not found in the records.")

# --- Print all student grades ---
print("\nAll Student Grades:")
for student, grade in students.items():
    print(f"{student}: {grade}")