#!/usr/bin/python3

#  A Python program that does takes a student name, colloct his/her scores in three subject - Mathematics, English, and Computer Science. Calculate their scores and tell them if they pass or fail.

pass_mark = 50


# TODO2: Collect their scores in Mathematics, English, and Computer Science.
def get_score(subject_name):
    while True:
        try:
            score = int(input(f"Enter {subject_name} Score: "))
            if score < 0 or score > 100:
                print("Invalid input: Score must be between 0 and 100")
                continue
            return score
            break
        except ValueError:
            print("Error: Enter a valid number")
            continue

def main():
    student_name = input("Enter your name: ")
    maths_score = get_score("Mathematics")
    eng_score = get_score("English")
    csc_score = get_score("Computer Science")


    total_score = maths_score + eng_score + csc_score
    avg_score = total_score / 3

# TODO4: Determines whether they passed, assuming a score of 50 or above in each subject is a pass.
    if maths_score >=  pass_mark and eng_score >= pass_mark and csc_score >= pass_mark:
        overall_res = f"Congratulation! You passed successfully."
    else:
        overall_res = f"Sorry you fail, didn't meet the requirement."
# TODO5: Prints the student's name, total, average, and overall result.
    print("<----- Here is the Summary of your Result ---->")
    print(f"{student_name}")
    print(f"- Total Score: {total_score}")
    print(f"- Average Score: {avg_score:.2f}")
    print(f"- Overall Result: {overall_res}")


if __name__=="__main__":
    main()
