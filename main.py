#!/usr/bin/python3

"""
A Python program that does takes a student name, collect his/her scores in three subject - Mathematics,
English, and Computer Science. Calculate their scores and tell them if they pass or fail.
"""

from models import Student
from storage import save_result


def get_score(subject_name: str) -> int:
    while True:
        try:
            score = int(input(f"Enter {subject_name} Score: "))
            if score < 0 or score > 100:
                print("Invalid input: Score must be between 0 and 100")
                continue
            return score
        except ValueError:
            print("Error: Enter a valid number")


def get_name() -> str:
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Error: Name cannot be empty")


def main():
    student_name = get_name()
    maths_score = get_score("Mathematics")
    eng_score = get_score("English")
    csc_score = get_score("Computer Science")


    student = Student(student_name, {
    "Mathematics": maths_score,
    "English": eng_score,
    "Computer Science": csc_score
})

    if student.has_passed():
        overall_res = "Congratulations! You passed successfully."
    else:
        overall_res = "Sorry you fail, didn't meet the requirement."

    print("<----- Here is the Summary of your Result ---->")
    print(f"{student_name}")
    print(f"- Total Score: {student.total()}")
    print(f"- Average Score: {student.average():.2f}")
    print(f"- Overall Result: {overall_res}")
    save_result(**student.to_dict())


if __name__ == "__main__":
    main()
