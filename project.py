from tabulate import tabulate

def main():
    print("\nvvksrma | Student Information Management System")
    running = True
    database, count = [], 0

    while running:
        action = get_input()

        if action == "V":
            view(database)
        elif action == "C":
            database, count = create(database, count)
        elif action == "U":
            database = update(database)
        elif action == "D":
            database = delete(database)
        elif action == "E":
            print("Exiting the system.")
            running = False


def get_input():
    """Display options and get user input."""
    instructions = [
        {"Key": "V", "Action": "View Students"},
        {"Key": "C", "Action": "Add a Student"},
        {"Key": "U", "Action": "Update a Student"},
        {"Key": "D", "Action": "Delete a Student"},
        {"Key": "E", "Action": "Exit"}
    ]

    while True:
        print(tabulate(instructions, headers="keys", tablefmt="rounded_outline"))
        action = input("What do you want to do?: ").upper()

        if action in ["V", "C", "U", "D", "E"]:
            return action
        else:
            print("Invalid key, try again.")


def view(data):
    """Display the list of students."""
    if data:
        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
    else:
        print("No student information available.")


def create(data, i):
    """Add a new student to the database."""
    name = input("Student Name: ")
    roll_no = input("Roll No: ")
    student_class = input("Class: ")
    i += 1
    data.append({"ID": i, "Name": name, "Roll No": roll_no, "Class": student_class})
    print("Student added successfully.")
    return data, i


def update(data):
    """Update an existing student's information."""
    if not data:
        print("No students to update.")
        return data

    numbers = [student["ID"] for student in data]

    while True:
        view(data)
        try:
            i = int(input("Which student would you like to update? (Enter ID): "))
            if i in numbers:
                break
            else:
                print("Invalid student ID, try again.")

        except ValueError:
            print("Invalid input, try again.")

    name = input("New Name (Leave blank to keep current): ")
    roll_no = input("New Roll No (Leave blank to keep current): ")
    student_class = input("New Class (Leave blank to keep current): ")

    for student in data:
        if student["ID"] == i:
            if name:
                student["Name"] = name
            if roll_no:
                student["Roll No"] = roll_no
            if student_class:
                student["Class"] = student_class
            print("Student updated successfully.")
            break

    return data


def delete(data):
    """Delete a student from the database."""
    if not data:
        print("No students to delete.")
        return data

    numbers = [student["ID"] for student in data]

    while True:
        view(data)
        try:
            i = int(input("Which student would you like to delete? (Enter ID): "))
            if i in numbers:
                break
            else:
                print("Invalid student ID, try again.")

        except ValueError:
            print("Invalid input, try again.")

    for j in range(len(data)):
        if data[j]["ID"] == i:
            del data[j]
            print("Student deleted successfully.")
            break

    return data


if __name__ == "__main__":
    main()
