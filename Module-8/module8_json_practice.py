"""
Jordan Dardar
Module 8 - JSON Practice
"""

import json


def print_students(student_list):
    """Loop through the list and print each student."""
    print()  # blank line for readability
    for student in student_list:
        first = student.get("F_Name", "")
        last = student.get("L_Name", "")
        sid = student.get("Student_ID", "")
        email = student.get("Email", "")
        print(f"{last}, {first} : ID = {sid}, Email = {email}")
    print()  # blank line at the end


def main():
    # --- Load the JSON file into a Python list (JSON load()) ---
    try:
        with open("student.json", "r") as infile:
            class_list = json.load(infile)
    except FileNotFoundError:
        print("Error: student.json file not found in this folder.")
        return

    # --- Original list notification and print ---
    print("This is the original Student list.")
    print_students(class_list)

    # --- Add your own record with append() ---
    new_student = {
        "F_Name": "Jordan",
        "L_Name": "Dardar",
        "Student_ID": 21462936,
        "Email": "jdardar@gmail.com"
    }

    class_list.append(new_student)

    # --- Updated list notification and print ---
    print("This is the updated Student list.")
    print_students(class_list)

    # --- Write updated data back to JSON file (JSON dump()) ---
    with open("student.json", "w") as outfile:
        json.dump(class_list, outfile, indent=4)

    print("The student.json file was updated.")


if __name__ == "__main__":
    main()
