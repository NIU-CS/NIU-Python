from rich import print

students = {
    "Amy": {"grades": [90, 85, 88], "age": 18},
    "Ben": {"grades": [70, 80, 89], "age": 20},
    "Cara": {"grades": [95, 92, 90], "age": 19}
}

if __name__ == "__main__":
    # add average grade to each student
    for student in students.values():
        student["average"] = sum(student["grades"]) / len(student["grades"])

    # find the student with the highest average grade
    top_student = max(students.items(), key=lambda item: item[1]["average"])
    print(f"Student grade student name: {top_student[0]}, "
          f"average grade: {top_student[1]['average']:.2f}, ")

    # sort students by average grade from highest to lowest
    sorted_students = sorted(students.items(), key=lambda item: item[1]["average"], reverse=True)
    print("\nSorted students by average grade:")
    for student_name, student in sorted_students:
        print(f"{student_name}: {student['average']:.2f}, Age: {student['age']}")
