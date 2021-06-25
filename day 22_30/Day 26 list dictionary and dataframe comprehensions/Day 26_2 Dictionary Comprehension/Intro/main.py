import random

names = ['Peter','Karen','Mollie', 'Alice','Poppy']

# create a dictionary from the list of names with a random number for the grades
student_grades = {student:random.randint(1,100) for student in names}
print(student_grades)


# Passed Students
passed_students = {student:grade for (student,grade) in student_grades.items() if grade >= 50 }
print(passed_students)