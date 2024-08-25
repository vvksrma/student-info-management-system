# Student Information Management System
#### Video Demo:  [Watch Here](<https://www.youtube.com/watch?v=V-P56ipmZ50>)
#### Description:

The **Student Information Management System** (SIMS) is a Python-based Command Line Interface (CLI) application designed to manage student details efficiently. This program allows users to:

- **View** the list of students.
- **Add** new students with their Name, Roll Number, and Class.
- **Update** existing student details.
- **Delete** students from the list.

The application uses the `tabulate` library to display data in a formatted table, making it easy to read and manage student information.

## Features

- **View Students:** Display a comprehensive list of all students.
- **Add Students:** Add new students with Name, Roll Number, and Class.
- **Update Students:** Update details of existing students.
- **Delete Students:** Remove students from the list.

## Installation

To use the Student Information Management System, follow these steps:

1. **Install Python:** Ensure Python is installed on your computer. Download it from [python.org](https://www.python.org/).

2. **Install Dependencies:** Install the required `tabulate` library using pip:
   ```bash
   pip install tabulate

## Usage
1. **Clone the Repository:**
```
git clone <repository_url>

cd <repository_directory>
```
2. **Run the Application:** Execute the script by running:

```
python <script_name>.py
```
3. **Select an Option:** Choose from the following menu options:

```
1. View Students
2. Add Student
3. Update Student
4. Delete Student
5. Exit
```
4. **Follow Prompts:** Enter the required information when prompted. For updating and deleting, provide the Roll Number of the student whose details you wish to modify.

## Code Breakdown
### Importing Libraries
```
from tabulate import tabulate
```
The `tabulate` library is used to format the student data into a table.

### Student Management System Class

```
class StudentManagementSystem:
    def __init__(self):
        self.students = []
```
The `StudentManagementSystem` class initializes an empty list for storing student records.

### Add Student
```
def add_student(self, name, roll_number, student_class):
    self.students.append({
        'Name': name,
        'Roll Number': roll_number,
        'Class': student_class
    })
```
Adds a new student's information to the list.

### View Students
```
def view_students(self):
    if not self.students:
        print("No students found.")
        return
    print(tabulate(self.students, headers="keys", tablefmt="grid"))
```
Displays the list of students in a formatted table.

### Update Student

```
def update_student(self, roll_number, name=None, student_class=None):
    for student in self.students:
        if student['Roll Number'] == roll_number:
            if name:
                student['Name'] = name
            if student_class:
                student['Class'] = student_class
            print("Student details updated successfully.")
            return
    print("Student not found.")
```
Updates details of a student based on their Roll Number.

### Delete Student

```
def delete_student(self, roll_number):
    for student in self.students:
        if student['Roll Number'] == roll_number:
            self.students.remove(student)
            print("Student removed successfully.")
            return
    print("Student not found.")
```
Removes a student from the list based on their Roll Number.

### Main Function
```
def main():
    system = StudentManagementSystem()
    while True:
        print("\nStudent Information Management System")
        print("1. View Students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            system.view_students()
        elif choice == '2':
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            student_class = input("Enter student class: ")
            system.add_student(name, roll_number, student_class)
            print("Student added successfully.")
        elif choice == '3':
            roll_number = input("Enter roll number of student to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            student_class = input("Enter new class (leave blank to keep current): ")
            system.update_student(roll_number, name or None, student_class or None)
        elif choice == '4':
            roll_number = input("Enter roll number of student to delete: ")
            system.delete_student(roll_number)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
```
### Example
Here is an example of how the application operates:

```
Student Information Management System
1. View Students
2. Add Student
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 2
Enter student name: John Doe
Enter roll number: 123
Enter student class: 10
Student added successfully.

Student Information Management System
1. View Students
2. Add Student
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 1
+-----------+-------------+-------------+
| Name      | Roll Number | Class       |
+-----------+-------------+-------------+
| John Doe  | 123         | 10          |
+-----------+-------------+-------------+

Student Information Management System
1. View Students
2. Add Student
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 3
Enter roll number of student to update: 123
Enter new name (leave blank to keep current): Jane Doe
Enter new class (leave blank to keep current): 
Student details updated successfully.

Student Information Management System
1. View Students
2. Add Student
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 1
+-----------+-------------+-------------+
| Name      | Roll Number | Class       |
+-----------+-------------+-------------+
| Jane Doe  | 123         | 10          |
+-----------+-------------+-------------+

Student Information Management System
1. View Students
2. Add Student
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 4
Enter roll number of student to delete: 123
Student removed successfully.

Student Information Management System
1. View Students
2. Add Student
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 5
Exiting the system.
```
### Conclusion
The Student Information Management System is a powerful CLI application for managing student records. It provides a user-friendly interface to view, add, update, and delete student information. The use of the `tabulate` library ensures that data is presented in a clear and organized manner.

Feel free to enhance the application with additional features or improvements based on your requirements.

