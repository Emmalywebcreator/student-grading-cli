#!/usr/bin/python3

"""
A Python program that does takes a student name, colloct his/her scores in three subject - Mathematics, English, and Computer Science. Calculate their scores and tell them if they pass or fail.
"""

PASS_MARK = 50


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


def has_passed(m_score: int, e_score: int, c_score: int) -> bool:
    return all(score >= PASS_MARK for score in (m_score, e_score, c_score))


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

    total_score = maths_score + eng_score + csc_score
    avg_score = total_score / 3

    if has_passed(maths_score, eng_score, csc_score):
        overall_res = "Congratulations! You passed successfully."
    else:
        overall_res = "Sorry you fail, didn't meet the requirement."

    print("<----- Here is the Summary of your Result ---->")
    print(f"{student_name}")
    print(f"- Total Score: {total_score}")
    print(f"- Average Score: {avg_score:.2f}")
    print(f"- Overall Result: {overall_res}")


if __name__ == "__main__":
    main()
