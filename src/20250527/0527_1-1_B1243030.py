from rich import print

Student1 = {
    "name": "John",
    "age": 21,
    "grades": [88, 91, 90],
    "major": "Electrical Engineering"
}

Student2 = {
    "name": "Brian",
    "age": 20,
    "grades": [93, 89, 92],
    "major": "Computer Science"
}

if __name__ == "__main__":
    student_info: dict = {
        "Student1": Student1,
    }

    student_info = dict(student_info, Student2=Student2)
    for student in student_info.values():
        student["average"] = sum(student["grades"]) / len(student["grades"])

    print("\nStudent Information:")
    for student_name, student in student_info.items():
        print(f"{student_name}: {student['name']}, \tAge: {student['age']}, \t"
              f"Major: {student['major']}, \tAverage Grade: {student['average']:.2f}")