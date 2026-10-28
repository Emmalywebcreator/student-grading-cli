#!/usr/bin/python3

#  A Python program that does takes a student name, colloct his/her scores in three subject - Mathematics, English, and Computer Science. Calculate their scores and tell them if they pass or fail.

pass_mark = 50

# TODO1: Colllect student's name and store it in a variable.

student_name = input("Enter your name: ")

# TODO2: Collect their scores in Mathematics, English, and Computer Science.
while True:
    maths_score = float(input("Enter your Mathematics score: "))
    if maths_score < 0 or maths_score > 100:
        print("Invalid score: Score must lies between 0 and 100")
        continue

    eng_score = float(input("Enter your English score: "))
    if eng_score < 0 or eng_score > 100:
        print("Invalid score: Score must lies between 0 and 100")
        continue
    csc_score = float(input("Enter your Computer Science score: "))
    if csc_score < 0 or csc_score > 100:
        print("Invalid score: Score must lies between 0 and 100")
        continue
    else:
        break
total_score = maths_score + eng_score + csc_score
avg_score = total_score / 3

# TODO4: Determines whether they passed, assuming a score of 50 or above in each subject is a pass.
if maths_score <  pass_mark or eng_score < pass_mark or csc_score < pass_mark:
    overall_res = f"Sorry you fail, didn't meet the requirement."
else:
    overall_res = f"Congratulation, you pass successfully"
# TODO5: Prints the student's name, total, average, and overall result.
print(f"{student_name} - Total Score: {total_score} Average Score: {avg_score} Overall Result: {overall_res}") 
# TODO6: Handles the situation where a score is ivalid, such as -5 or 120
