#Raymundo Sanchez
#CSS 225
#Oct 23,2020
#lab

# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average   Grade
# 90+	     A
# 80-89	     B
# 70-79	     C
# 60-69	     D
# 0-59	     F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

avg = (exam_one + exam_two + exam_three) / 3

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("Average: " + str(avg))
print("Grade: " + letter_grade)
#I added the word "or" and also included the letter grade == "D"
#this helped it know that if you get a "d" as a letter grade you would fail.
if letter_grade == "F" or letter_grade == "D":
    print("Student is failing.")
else:
    print("Student is passing.")
